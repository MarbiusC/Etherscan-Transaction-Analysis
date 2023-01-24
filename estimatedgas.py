import requests
import pandas as pd
from datetime import datetime, timedelta

# Etherscan API endpoint
api_url = 'https://api.etherscan.io/api?'
api_key = 'YA3DIE4BCUURV9P5HJ45N79TVTC6H8H6H7'

# Fetch historical gas prices for the past 2 weeks
gas_prices = []
for i in range(14):
    params = {
        'module': 'proxy',
        'action': 'eth_estimateGas',
        'apikey': api_key,
        'to': '0x742d35Cc6634C0532925a3b844Bc454e4438f44e', # Address of the contract to estimate gas for
        'value': '0x0', # Value to send with the transaction
        'data': '0x0', # Data to send with the transaction
    }
    response = requests.get(api_url, params=params)
    data = response.json()
    time = (datetime.now() - timedelta(days=i)).strftime("%Y-%m-%d %H:%M:%S")
    gas_prices.append({
        'time': time,
        'gas_price': data['result']
    })

# Convert data to a dataframe
df = pd.DataFrame(gas_prices)

# Write the dataframe to a CSV file
df.to_csv('gas_prices.csv', index=False)
