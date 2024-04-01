import json

with open("25_python_working_with_json/data_json.json", "r") as file:
  data_jkt = json.load(file)

print(data_jkt[0]["independent"])
print(type(data_jkt))

print(json.dumps(data_jkt, indent=4))