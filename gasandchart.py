import requests
import pandas as pd
import matplotlib.pyplot as plt

# Etherscan API endpoint
api_url = 'https://api.etherscan.io/api?'
api_key = 'YA3DIE4BCUURV9P5HJ45N79TVTC6H8H6H7'

# Fetch historical gas prices for the past 2 weeks
gas_prices = []
for i in range(14):
    params = {
        'module': 'proxy',
        'action': 'eth_estimateGas',
        'to': '0x742d35Cc6634C0532925a3b844Bc454e4438f44e',
        'value': '0x0',
        'apikey': api_key,
        'blockno': 'latest',
        'offset': i
    }
    response = requests.get(api_url, params=params)
    data = response.json()
    time = data.get('timeStamp', 'N/A')
    gas_price = data['result']
    gas_prices.append({
        'time': time,
        'gas_price': gas_price
    })

# Convert data to a dataframe
df = pd.DataFrame(gas_prices)

# Write the dataframe to a csv file
df.to_csv('gas_prices.csv', index=False)

# Plot the data
plt.plot(df['time'], df['gas_price'])
plt.xlabel('Time')
plt.ylabel('Gas Price (wei)')
plt.show()
