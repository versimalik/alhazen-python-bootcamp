#ordered
#changeable
#dia pake {}
#pake key value
#do not allow duplicates
student = {"name": "Sifa", "address" : "Jakarta"}

car = {
    "model" : "truck",
    "brand" : "ford",
    "brand" : "ford",
    "year" : 2010
}
print(type(student))
print(student)
print(type(car))
print(car)




#ACCESS DICTIONARY KEY-VALUES
#print all keys in student dictionary
print(student.keys())
#print student name by calling "name" key
print(student["name"])

car = {
    "model" : "truck",
    "brand" : "ford",
    "brand" : "ford",
    "year" : 2010
}
# print(car.keys())
print(car["model"])


#DICTIONARY MANIPULATIONS
#add new item (key:value)
car["color"] = "red"
print(car)
#modify existing item (key:value)
car.update({"model" : ["minibus", "telolet"]})
#remove spicific item
#using .pop() followed by its key
car.pop("model")
print(car)
#remove existing last item
car.popitem()

car = {
    "model" : "truck",
    "brand" : "ford",
    "year" : 2010
}
# car["color"] = "red"
car.update({"model" :["minibus", "truck"]})
car.pop("model")
car.popitem()
print(car)

#dict for dictionary constructor
student = dict(name = "Jamal", address = "Jakarta")


