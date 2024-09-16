import yfinance as yf
import datetime
from math import log, sqrt, exp
from scipy.stats import norm
import pandas as pd
import numpy as np
import json
import os


def to_timestamp(date_str):
    return int(datetime.datetime.strptime(date_str, "%Y-%m-%d").timestamp())


class Option:
    def __init__(self, option_data, underlying_price, expiration_date, option_type, risk_free_rate, dividend_yield):
        self.contract_symbol = option_data['contractSymbol']
        self.last_trade_date = option_data.get('lastTradeDate', '-')
        self.strike = option_data.get('strike', -1)
        self.last_price = option_data.get('lastPrice', '-')
        self.bid = option_data.get('bid', '-')
        self.ask = option_data.get('ask', '-')
        self.change = option_data.get('change', '-')
        self.percent_change = option_data.get('percentChange', '-')
        self.volume = option_data.get('volume', '-')
        self.open_interest = option_data.get('openInterest', '-')
        self.implied_volatility = option_data.get('impliedVolatility', -1)
        # Do not divide implied volatility by 100; yfinance provides it as a decimal already
        self.implied_volatility = float(self.implied_volatility)

        self.underlying_price = underlying_price
        self.expiration_date = expiration_date
        self.option_type = option_type.lower()
        self.risk_free_rate = risk_free_rate  # Note to Dev: this is expected as a decimal (e.g., 0.05 for 5%)
        self.dividend_yield = dividend_yield

        # Cache for Greeks
        self._delta = None
        self._gamma = None
        self._theta = None
        self._vega = None
        self._rho = None

    def _calculate_d1_d2(self):
        S = self.underlying_price
        K = self.strike
        t = (self.expiration_date - datetime.datetime.now()).total_seconds() / (365 * 24 * 3600)
        if t <= 0:
            t = 1e-8  # Avoid division by zero
        r = self.risk_free_rate
        q = self.dividend_yield
        v = self.implied_volatility
        if v is None or v <= 0:
            v = 1e-8  # Avoid division by zero

        d1 = (log(S / K) + (r - q + 0.5 * v ** 2) * t) / (v * sqrt(t))
        d2 = d1 - v * sqrt(t)
        return d1, d2, t

    def delta(self):
        if self._delta is not None:
            return self._delta
        d1, _, t = self._calculate_d1_d2()
        if self.option_type == 'c':
            self._delta = exp(-self.dividend_yield * t) * norm.cdf(d1)
        else:
            self._delta = -exp(-self.dividend_yield * t) * norm.cdf(-d1)
        return self._delta

    def gamma(self):
        if self._gamma is not None:
            return self._gamma
        d1, _, t = self._calculate_d1_d2()
        S = self.underlying_price
        v = self.implied_volatility
        self._gamma = exp(-self.dividend_yield * t) * norm.pdf(d1) / (S * v * sqrt(t))
        return self._gamma

    def theta(self):
        if self._theta is not None:
            return self._theta
        d1, d2, t = self._calculate_d1_d2()
        S = self.underlying_price
        K = self.strike
        r = self.risk_free_rate
        q = self.dividend_yield
        v = self.implied_volatility
        if self.option_type == 'c':
            self._theta = (- (S * v * exp(-q * t) * norm.pdf(d1)) / (2 * sqrt(t))
                           - r * K * exp(-r * t) * norm.cdf(d2)
                           + q * S * exp(-q * t) * norm.cdf(d1)) / 365
        else:
            self._theta = (- (S * v * exp(-q * t) * norm.pdf(d1)) / (2 * sqrt(t))
                           + r * K * exp(-r * t) * norm.cdf(-d2)
                           - q * S * exp(-q * t) * norm.cdf(-d1)) / 365
        return self._theta

    def vega(self):
        if self._vega is not None:
            return self._vega
        d1, _, t = self._calculate_d1_d2()
        S = self.underlying_price
        self._vega = S * exp(-self.dividend_yield * t) * sqrt(t) * norm.pdf(d1) / 100
        return self._vega

    def rho(self):
        if self._rho is not None:
            return self._rho
        _, d2, t = self._calculate_d1_d2()
        K = self.strike
        r = self.risk_free_rate
        if self.option_type == 'c':
            self._rho = K * t * exp(-r * t) * norm.cdf(d2) / 100
        else:
            self._rho = -K * t * exp(-r * t) * norm.cdf(-d2) / 100
        return self._rho

    def compute_all_greeks(self):
        self.delta()
        self.gamma()
        self.theta()
        self.vega()
        self.rho()


class OptionChain:
    def __init__(self, stock_ticker, option_type, dividend_yield=0.0, expiration_date=None, risk_free_rate=0.05):
        self.stock_ticker = stock_ticker
        self.option_type = option_type.lower()
        self.dividend_yield = dividend_yield
        self.expiration_date = expiration_date
        self.risk_free_rate = risk_free_rate
        self.options = []
        self.underlying_price = None
        self.fetch_options()

    def fetch_options(self):
        ticker = yf.Ticker(self.stock_ticker)
        hist = ticker.history(period='1d')
        if hist.empty:
            print('Error fetching historical data for the underlying stock.')
            return
        self.underlying_price = hist['Close'].iloc[-1]  # Note to Dev: this will use .iloc[-1] for positional indexing

        expirations = ticker.options
        if not expirations:
            print('Error. No options for this symbol!')
            return

        if self.expiration_date:
            if self.expiration_date in expirations:
                exp_date = self.expiration_date
            else:
                print('Error. Expiration date not available.')
                return
        else:
            exp_date = expirations[0]

        self.expiration_date = datetime.datetime.strptime(exp_date, '%Y-%m-%d')

        options_chain = ticker.option_chain(exp_date)
        if self.option_type == 'c':
            options_list = options_chain.calls.to_dict('records')
        else:
            options_list = options_chain.puts.to_dict('records')

        for option_data in options_list:
            option = Option(
                option_data,
                self.underlying_price,
                self.expiration_date,
                self.option_type,
                self.risk_free_rate,
                self.dividend_yield
            )
            self.options.append(option)

    def compute_all_greeks(self):
        for option in self.options:
            option.compute_all_greeks()

    def get_options_data(self):
        data = []
        for option in self.options:
            data.append({
                'Symbol': option.contract_symbol,
                'Last Trade': option.last_trade_date,
                'Strike': option.strike,
                'Last Price': option.last_price,
                'Bid': option.bid,
                'Ask': option.ask,
                'Change': option.change,
                '% Change': option.percent_change,
                'Volume': option.volume,
                'Open Interest': option.open_interest,
                'Implied Volatility': option.implied_volatility
            })
        return pd.DataFrame(data)

    def get_greeks_data(self):
        data = []
        for option in self.options:
            data.append({
                'Symbol': option.contract_symbol,
                'Strike': option.strike,
                'Last Price': option.last_price,
                'Bid': option.bid,
                'Ask': option.ask,
                'Implied Volatility': option.implied_volatility,
                'Delta': option.delta(),
                'Gamma': option.gamma(),
                'Theta': option.theta(),
                'Vega': option.vega(),
                'Rho': option.rho()
            })
        df = pd.DataFrame(data)
        # Note to Dev: this will convert NumPy float64 to native Python floats for a cleaner output, do not get rid of
        # this unless deprecated
        numeric_columns = ['Strike', 'Last Price', 'Bid', 'Ask', 'Implied Volatility', 'Delta', 'Gamma', 'Theta', 'Vega', 'Rho']
        df[numeric_columns] = df[numeric_columns].applymap(lambda x: float(x) if isinstance(x, (float, int, np.float64)) else x)
        return df


class BSOptionPricing:
    @staticmethod
    def get_chain_greeks(stock_ticker, dividend_yield, option_type, risk_free_rate=0.05):
        chain = OptionChain(stock_ticker, option_type, dividend_yield, risk_free_rate=risk_free_rate)
        chain.compute_all_greeks()
        return chain.get_greeks_data()

    @staticmethod
    def get_chain_greeks_date(stock_ticker, dividend_yield, option_type, expiration_date, risk_free_rate=0.05):
        chain = OptionChain(stock_ticker, option_type, dividend_yield, expiration_date, risk_free_rate)
        chain.compute_all_greeks()
        return chain.get_greeks_data()

    @staticmethod
    def get_option_greeks(stock_ticker, expiration_date, option_type, strike, dividend_yield, risk_free_rate=0.05):
        chain = OptionChain(stock_ticker, option_type, dividend_yield, expiration_date, risk_free_rate)
        option = next((opt for opt in chain.options if opt.strike == strike), None)
        if option:
            option.compute_all_greeks()
            return {
                'Symbol': option.contract_symbol,
                'Strike': float(option.strike),
                'Last Price': float(option.last_price),
                'Bid': float(option.bid),
                'Ask': float(option.ask),
                'Implied Volatility': float(option.implied_volatility),
                'Delta': float(option.delta()),
                'Gamma': float(option.gamma()),
                'Theta': float(option.theta()),
                'Vega': float(option.vega()),
                'Rho': float(option.rho())
            }
        else:
            print('Option not found.')
            return None

    @staticmethod
    def get_expiration_dates(stock_ticker):
        ticker = yf.Ticker(stock_ticker)
        expirations = ticker.options
        return expirations

    @staticmethod
    def get_underlying_price(stock_ticker):
        ticker = yf.Ticker(stock_ticker)
        hist = ticker.history(period='1d')
        if hist.empty:
            print('Error fetching historical data for the underlying stock.')
            return None
        price = hist['Close'].iloc[-1]  # Note to dev: this will use .iloc[-1] for positional indexing
        return price
