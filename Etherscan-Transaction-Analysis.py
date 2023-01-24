#Etherscan Transaction Analysis
#Determining the most frequent time of day transactions happen

import requests
import json

# Etherscan API endpoint
url = "https://api.etherscan.io/api?"

# Etherscan API key
api_key = "YA3DIE4BCUURV9P5HJ45N79TVTC6H8H6H7"

# Starting and ending block numbers
start_block = 16470000
end_block = 16471525

# List to store block data
blocks = []

# Loop through all the blocks
for block_number in range(start_block, end_block + 1):
    # Send GET request totherscan API
    params = {'module': 'block', 'action': 'getblock', 'blockno': block_number, 'apikey': api_key}
    response = requests.get(url, params=params)
    # Parse response as JSON
    data = response.json()
    # Extract block data from JSON
    if data['status'] == "1":
        blocks.append(data['result'])
    else:
        print("No data found for block {}".format(block_number))

# Write block data to a JSON file
with open('blocks.json', 'w') as outfile:
    json.dump(blocks, outfile)
