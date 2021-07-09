import json

with open('conf.json','r') as f:
    config = json.load(f)

print(config['name']) # value_last
print(config['birth'])