import requests
import sys
import json


if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

api_key = "YourApiKey" 
url = f"https://rest.coincap.io/v3/assets/bitcoin?apiKey={api_key}"
try:
    bitcoin=float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

try:
    response=requests.get(url)
    data=response.json()
    price=float(data["data"]["priceUsd"])
    total=bitcoin*price
    print(f"${total:,.4f}")
    
except requests.RequestException:
    sys.exit("Network error")






