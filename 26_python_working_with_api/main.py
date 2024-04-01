import requests
import json

api_url = "https://jsonplaceholder.typicode.com/todos"

response = requests.get(api_url)

print(response)

data = response.json()

# print(data)
print(type(data))

for todo in data:
  if todo["completed"] == True:
    json_obj = json.dumps(todo, indent=4)
    print(json_obj)


api_jadwal = "https://api.myquran.com/v2/sholat/jadwal/1301/2024/04/01"

res_jadwal = requests.get(api_jadwal)

data_jadwal = res_jadwal.json()
print(data_jadwal)