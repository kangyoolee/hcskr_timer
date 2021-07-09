import json

with open('config.json','r') as f:
    config = json.load(f)

print(config['1st_key']) # value_last