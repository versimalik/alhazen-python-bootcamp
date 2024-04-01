import json

employee_string = '''
{
  "firstName" : "Jaka",
  "lastName" : "Antara",
  "age" : 35,
  "hobbies" : ["Swimming", "Archery"]
}
'''

print(employee_string)

# Serialize Json
data = {
  "employees" :
    [
      {
        "firstName" : "Jhon",
        "lastName" : "Doe"
      },
      {
        "firstName" : "Fatih",
        "lastName" : "Faruq"
      },
      {
        "firstName" : "Hamzah",
        "lastName" : "Abdul Hakim"
      },
    ]
}

print(data)
print(type(data))

with open("25_python_working_with_json/data_file.json", "w") as file:
  json.dump(data, file, indent=2)
  

print(json.dumps(data, indent=4))
print(type(json.dumps(data, indent=4))) # str

# Deserialize Json
print(100*"=")
print("Deserialize Json")
employee_dict = json.loads(employee_string)
print(employee_dict)
print(type(employee_dict))
print(employee_dict["hobbies"])

with open("25_python_working_with_json/data_file.json", "r") as file:
  py_data = json.load(file)
  
print(py_data)
print(type(py_data))




