# MarketQuant
![PyPI - Version](https://img.shields.io/pypi/v/marketquant) ![PyPI - Downloads](https://img.shields.io/pypi/dm/marketquant) ![Read the Docs](https://img.shields.io/readthedocs/marketquant?style=flat)  
A quantitative market analysis tool builder library.

[PyPI](https://pypi.org/project/marketquant/), [Read the Docs](https://marketquant.readthedocs.io), [Github](https://github.com/maxheltzel/MarketQuant).

---

## Installation 
`pip install marketquant`  
*You may need to use `pip3` instead of `pip`*

---

## Quick setup
1. Set up your developer account or API access.
   - You may need to configure your data provider keys in a `.env` file.
2. Install packages
   - Install `marketquant` and any required dependencies:
     ```sh
     pip install marketquant
     ```
   - *You may need to use `pip3` instead of `pip`*
3. Examples of how to use the client are in the `examples/` folder (add your keys in the `.env` file).  
```python
import marketquant

engine = marketquant.TradingEngine(
    data_provider="yahoo",
    ticker="SPY",
    start_date="2023-01-01",
    end_date="2024-08-01",
    candle_aggregation="1d",
    starting_balance=100000,
    shares=100
)

print(engine.run_strategy())
What can this program do?
Run trading simulations with custom strategies
Authenticate and access APIs (Yahoo Finance, Schwab, etc.)
Automatic token updates and real-time data streaming
Functions for API calls and customized strategy development
TBD
Paper trading client
More real-time data streaming support
Youtube Tutorials
Getting Started with MarketQuant
Custom Strategies with MarketQuant
License
Distributed under the MPL-2.0 License. See LICENSE for more information.

Contact
Max Heltzel - maxheltzel@gmail.com
Project Link: https://github.com/maxheltzel/MarketQuant

python
Copy code

### Notes:
- Replace the `marketquant` with your project’s name or any other identifiers.
- Ensure that all provided links (e.g., GitHub, PyPI, YouTube) match the real ones.
