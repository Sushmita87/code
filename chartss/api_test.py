import json
import requests
resp= requests.get("https://gist.githubusercontent.com/LichAmnesia/94a768257bb62e4d527cb265777d725a/raw/2354e3a65e7247ea32372057f6b9a4491a1056c8/stock_market_api_1.py")
data=resp.json()
print(data)
