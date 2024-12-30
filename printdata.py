import pandas as pd
import json

with open('data.json', 'r') as file:
    data = json.load(file)


for table_name, table_data in data.items():
    print(f"\n{table_name}")
    df = pd.DataFrame.from_dict(table_data, orient='index')
    print(df)
