import requests
import json

url = "https://restcountries.com/v3.1/capital/jakarta"

response = requests.get(url)

data = response.json()

print(json.dumps(data, indent=4))