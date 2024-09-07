<!-- PROJECT SHIELDS -->
[![Contributors][contributors-shield]][contributors-url] [![Forks][forks-shield]][forks-url] [![Stargazers][stars-shield]][stars-url] [![Issues][issues-shield]][issues-url] [![License][license-shield]][license-url] [![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO --> <br /> <div align="center"> <a href="https://github.com/maxheltzel/MarketQuant"> <img src="images/logo.png" alt="Logo" width="80" height="80"> </a> <h3 align="center">MarketQuant</h3> <p align="center"> A powerful quantitative market analysis tool for Python! <br /> <a href="https://github.com/maxheltzel/MarketQuant"><strong>Explore the docs »</strong></a> <br /> <br /> <a href="https://github.com/maxheltzel/MarketQuant">View Demo</a> · <a href="https://github.com/maxheltzel/MarketQuant/issues/new?labels=bug">Report Bug</a> · <a href="https://github.com/maxheltzel/MarketQuant/issues/new?labels=enhancement">Request Feature</a> </p> </div> <!-- TABLE OF CONTENTS --> <details> <summary>Table of Contents</summary> <ol> <li><a href="#about-the-project">About The Project</a></li> <li><a href="#built-with">Built With</a></li> <li><a href="#getting-started">Getting Started</a></li> <li><a href="#usage">Usage</a></li> <li><a href="#roadmap">Roadmap</a></li> <li><a href="#contributing">Contributing</a></li> <li><a href="#license">License</a></li> <li><a href="#contact">Contact</a></li> <li><a href="#acknowledgments">Acknowledgments</a></li> </ol> </details> <!-- ABOUT THE PROJECT -->
About The Project
![Product Screenshot][product-screenshot]

MarketQuant is a Python library designed to simplify the creation, simulation, and analysis of market strategies. Built for quants, traders, and developers, MarketQuant empowers users to focus on strategy development while providing powerful tools to access market data, indicators, and backtesting functionalities.

Key features:

Strategy Simulation: Test your trading ideas.
Built-in Indicators: Access popular indicators like MACD, RSI, etc.
Multiple Data Providers: Get market data from Yahoo Finance, Schwab, and more.
Advanced Charting: Visualize strategies with interactive charts.
<p align="right">(<a href="#readme-top">back to top</a>)</p>
Built With
MarketQuant is built with the following libraries:

Pandas
Matplotlib
mplfinance
mplcursors
Yahoo Finance
<p align="right">(<a href="#readme-top">back to top</a>)</p> <!-- GETTING STARTED -->
Getting Started
To get started with MarketQuant, follow these instructions to install and set up the library locally.

Prerequisites
Ensure you have Python 3.x and pip installed on your machine.

Installation
Clone the repo

sh
Copy code
git clone https://github.com/maxheltzel/MarketQuant.git
Install dependencies

sh
Copy code
pip install -r requirements.txt
Install the MarketQuant package from PyPI:

sh
Copy code
pip install MarketQuant
<p align="right">(<a href="#readme-top">back to top</a>)</p> <!-- USAGE -->
Usage
Here’s an example of running a MACD strategy with the MarketQuant library:

python
Copy code
from MarketQuant.strategy_simulator import TradingEngine
from MarketQuant.indicators.macd import MACDIndicator
from MarketQuant.strategies.macd_strategy import MACDStrategy

# Initialize the trading engine
engine = TradingEngine(
    data_provider="yahoo",
    ticker="SPY",
    start_date="2023-01-01",
    end_date="2024-08-01",
    candle_aggregation="1d",
    starting_balance=100000,
    shares=100
)

# Initialize and run the strategy
macd = MACDIndicator()
strategy = MACDStrategy(engine, macd)
strategy.run()

# Print results
engine.print_results()
<p align="right">(<a href="#readme-top">back to top</a>)</p> <!-- ROADMAP -->
Roadmap
 Basic strategy support (MACD, RSI, etc.)
 Expand data provider support
 Add more customizable indicators
 Integrate live trading
See the open issues for a list of proposed features and known issues.

<p align="right">(<a href="#readme-top">back to top</a>)</p> <!-- CONTRIBUTING -->
Contributing
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.

Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)
Commit your Changes (git commit -m 'Add some AmazingFeature')
Push to the Branch (git push origin feature/AmazingFeature)
Open a Pull Request
<p align="right">(<a href="#readme-top">back to top</a>)</p> <!-- LICENSE -->
License
Distributed under the Mozilla Public License 2.0. See LICENSE.txt for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p> <!-- CONTACT -->
Contact
Max Heltzel - Email

Project Link: https://github.com/maxheltzel/MarketQuant

<p align="right">(<a href="#readme-top">back to top</a>)</p> <!-- ACKNOWLEDGMENTS -->
Acknowledgments
Choose an Open Source License
Img Shields
Font Awesome
GitHub Emoji Cheat Sheet
<p align="right">(<a href="#readme-top">back to top</a>)</p>
