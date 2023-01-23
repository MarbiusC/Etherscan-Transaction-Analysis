#Etherscan Transaction Analysis
#Determining the most frequent time of day transactions happen

import requests
import json

# Etherscan API endpoint
url = "https://api.etherscan.io/api"

# Etherscan API key
api_key = "YA3DIE4BCUURV9P5HJ45N79TVTC6H8H6H7"

# Starting and ending block numbers
start_block = 16470000
end_block = 16471525

# Send GET request to Etherscan API
params = {'module': 'block', 'action': 'getblockrange', 'startblock': start_block, 'endblock': end_block, 'apikey': api_key}
response = requests.get(url, params=params)

# Parse response as JSON
data = response.json()

# Extract block data from JSON
if data['status'] == "1":
    blocks = data["result"]
else:
    print("No data found for block range {}-{}".format(start_block, end_block))

# Write block data to a JSON file
with open('blocks.json', 'w') as outfile:
    json.dump(blocks, outfile)
