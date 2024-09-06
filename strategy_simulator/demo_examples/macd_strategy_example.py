#!/usr/bin/env python3
from MarketQuant.strategy_simulator import TradingEngine


def calculate_macd(data, short_period=12, long_period=26, signal_period=9):
    data['EMA_short'] = data['Close'].ewm(span=short_period, adjust=False).mean()
    data['EMA_long'] = data['Close'].ewm(span=long_period, adjust=False).mean()

    data['MACD'] = data['EMA_short'] - data['EMA_long']
    data['Signal'] = data['MACD'].ewm(span=signal_period, adjust=False).mean()

    return data


def macd_strategy(trading_engine):
    data = trading_engine.data_engine.fetch_data()
    data = calculate_macd(data)
    for i in range(1, len(data)):
        date = data['Date'][i]
        macd = data['MACD'][i]
        signal = data['Signal'][i]
        previous_macd = data['MACD'][i - 1]
        previous_signal = data['Signal'][i - 1]

        # Check for cover signal (MACD crosses above signal line) to close the short
        if previous_macd <= previous_signal and macd > signal:
            price = data['Close'][i]
            # If in a short position, cover it
            if trading_engine.simulator.account_manager.positions.get('long', {}).get('quantity', 0) > 0:
                trading_engine.simulator.sell(date, price, trading_engine.shares)

        # Check for short signal (MACD crosses below signal line)
        elif previous_macd >= previous_signal and macd < signal:
            price = data['Close'][i]
            # Short the stock
            trading_engine.simulator.buy(date, price, trading_engine.shares)



def main():

    # User Note: Initialize the trading core with your params for data_provider, ticker, start_date, end_date,
    # candle_aggregation, starting_balance, and shares below.
    engine = TradingEngine(
        data_provider="yahoo",
        ticker="SPY",
        start_date="2023-01-01",
        end_date="2024-08-01",
        candle_aggregation="1d",
        starting_balance=100000,
        shares=100,
        print_tradehistory=False,
        print_pnl=True,
        print_balance=True,
        print_buypower=True,
        print_unrealizedpnl=True,
        print_timecomplexity=True,
        chart=True
    )

    # Example: This will run the MACD strategy
    macd_strategy(engine)
    # Example: This prints the results of the enabled outputs
    engine.print_results()


if __name__ == "__main__":
    main()
