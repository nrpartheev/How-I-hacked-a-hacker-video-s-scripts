import requests
import json


database_url = ' -- REDACTED -- '

def fetch_data():
    try:
        response = requests.get(f"{database_url}/.json") 
        if response.status_code == 200:
            print(response.text)
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"An error occurred: {e}"

def save_data_to_file(data, filename="data.json"):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)  
        print(f"Data successfully saved to {filename}")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

if __name__ == "__main__":
    data = fetch_data()
    print(data)
    if isinstance(data, dict): 
        save_data_to_file(data)
    else:
        print(f"Failed to fetch data: {data}")
