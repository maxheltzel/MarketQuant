# Schwab-API-Python
![PyPI - Version](https://img.shields.io/pypi/v/schwabdev) ![PyPI - Downloads](https://img.shields.io/pypi/dm/marketquant) [![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/donate/?business=8VDFKHMBFSC2Q&no_recurring=0&currency_code=USD) ![YouTube Video Views](https://img.shields.io/youtube/views/kHbom0KIJwc?style=flat&logo=youtube)  
This is the official and updated python MarketQuant repository.
[PyPI](https://pypi.org/project/schwabdev/), [Youtube](https://youtube.com/playlist?list=PLs4JLWxBQIxpbvCj__DjAc0RRTlBz-TR8), [Github](https://github.com/tylerebowers/Schwab-API-Python).

## Installation 
`pip install schwabdev requests websockets`  
*You may need to use `pip3` instead of `pip`*

## Quick setup
1. Setup your Schwab developer account [here](https://beta-developer.schwab.com/).
   - Create a new Schwab individual developer app with callback url "https://127.0.0.1" (case sensitive) 
   - Wait until the status is "Ready for use", note that "Approved - Pending" will not work.
   - Enable TOS (Thinkorswim) for your Schwab account, it is needed for orders and other api calls.
2. Install packages
   - Install schwabdev and requirements `pip install schwabdev requests websockets`
   - *You may need to use `pip3` instead of `pip`*
3. Examples on how to use the client are in the `examples/` folder (add your keys in the .env file)  
   - The first time you run you will have to sign in to your Schwab account using the generated link in the terminal. After signing in, agree to the terms, and select account(s). Then you will have to copy the link in the address bar and paste it into the terminal. 
   - Questions? - join the [Discord group](https://discord.gg/m7SSjr9rs9).  
```py
import schwabdev #import the package

client = schwabdev.Client('Your app key', 'Your app secret')  #create a client

print(client.account_linked().json()) #make api calls
```

## What can this program do?
 - Authenticate and access the api 
 - Auto "access token" updates.
 - Functions for all api functions (examples in `examples/api_demo.py`)
 - Stream real-time data with a customizable response handler (examples in `examples/stream_demo.py`)
 ### TBD 
 - Paper trading client
 - Automatic refresh token updates. (Waiting for Schwab implementation)
### Notes
The schwabdev folder contains code for main operations:     
 - `api.py` contains functions relating to api calls, requests, and automatic token checker threads.
 - `stream.py` contains functions for streaming data from websockets.

## Youtube Tutorials
1. [Authentication and Requests](https://www.youtube.com/watch?v=kHbom0KIJwc&ab_channel=TylerBowers) *Github code has significantly changed since this video*
2. [Streaming Real-time Data](https://www.youtube.com/watch?v=t7F2dUecgWc&list=PLs4JLWxBQIxpbvCj__DjAc0RRTlBz-TR8&index=2&ab_channel=TylerBowers)

## MIT License

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
