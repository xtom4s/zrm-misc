from helpers import helpers as hl
import json

"""
Script for fecthing Tenderly simulation events for ZRM payloads
    Generates a nice payload with event data

The TENDERLY_ID is obtained by simulating the payload execution form the Avatar Safe using Tx Builder app
    It should be replaced in its corresponding place
"""

TENDERLY_ID = "Tenderly ID"
TENDERLY_URL = f"https://api.tenderly.co/api/v1/public/account/safe/project/safe-apps/simulate/{TENDERLY_ID}"

print('-------------------------')
print('-----Making Request -----')
print('-------------------------')

tenderly_sim_data = hl.fetch_tenderly_simulation_data(TENDERLY_URL)

print('')
print('------------------------')
print('------Request Done------')
print('------------------------')

events_json = tenderly_sim_data['transaction']['transaction_info']['call_trace']['logs']

data = []  # To build the json

for event_id, event in enumerate(events_json):    
    
    event_data = {
        'id': event_id,
        **hl.transform_tenderly_simulation_data(event)
    }
    data.append(event_data)

with open('payload_events.json', 'w') as file:  # Saves in current directory
    json.dump(data, file, indent=4)