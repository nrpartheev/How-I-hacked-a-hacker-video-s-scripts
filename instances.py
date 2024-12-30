import json
from datetime import datetime 



with open('data.json', 'r') as file:
    data = json.load(file)


for i in data:
    print(i)
