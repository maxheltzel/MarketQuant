<p align="center">
  <img src="https://github.com/maxheltzel/MarketQuant/blob/main/marketquant/MarketQuant_Logo.png?raw=true" width="300"/>
</p>

<p align="center">
  <img src="https://img.shields.io/pypi/v/marketquant" alt="PyPI - Version"/> 
  <img src="https://img.shields.io/pypi/dm/marketquant" alt="PyPI - Downloads"/> 
  <a href="https://paypal.me/maxheltzel2?country.x=US&locale.x=en_US">
    <img src="https://img.shields.io/badge/Donate-PayPal-green.svg" alt="Donate"/>
  </a>
</p>

---

This is the official and updated Python MarketQuant repository.

## Installation 
`pip install MarketQuant matplotlib numpy pandas mplfinance scipy mplcursors yfinance`  
*You may need to use `pip3` instead of `pip`*


## Schwab Quick setup
1. Setup your Schwab developer account [here](https://beta-developer.schwab.com/).
   - Create a new Schwab individual developer app with callback url "https://127.0.0.1" (case sensitive) 
   - Wait until the status is "Ready for use", note that "Approved - Pending" will not work.
   - Enable TOS (Thinkorswim) for your Schwab account, it is needed for orders and other api calls.
3. Why do I need to do this?
   - This will allow you to utilize the streaming and data tools that require a more nuanced data provider.
   - More data providers will be added in future updates.
   - You do not need a schwab account to utilize the Strategy Simulator. This uses data derived from Yahoo.


## What can this program do?
 - Build and simulate trading strategies using the TradingEngine class.
 - Utilize market data tools to create algorithms, strategies, or anything you can think of within the scope.
 - Charts your trades and outputs your strategy performance.
 - Extensible Framework to allow for complete customization.
 - Constantly adding more tools and features.

 ### TBD 
 - Paper trading client.
 - Charles Schwab API implementation to the Data Engine for the Simulator.
 - Bring over and configure quantitative tools to the repo.
 - Add YouTube tutorials for the library.

### Notes
The MarketQuant folder has all the code for the repo.

## Youtube Tutorials
1. [MarketQuant Installation Tutorial](https://youtu.be/C0Al9bn_FcA?si=g3uw3iX0LUHbvJen)



---

### Mozilla Public License 2.0
This Source Code Form is subject to the terms of the Mozilla Public License, v. 2.0. If a copy of the MPL was not distributed with this file, You can obtain one at:

https://mozilla.org/MPL/2.0/

Software distributed under the License is distributed on an "AS IS" basis, WITHOUT WARRANTY OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
