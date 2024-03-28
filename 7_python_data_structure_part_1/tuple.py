#tuple item is stored in round bracket
numbers = (0,1,2,3,4,5,6,7,8,9)
print(type(numbers))
print(len(numbers))



#tuple item is stored in round bracket
numbers = (1,2,3,4,5,6,7,8,9)
#access item by calling item index
#index is started form 0, NOT from 1
print(numbers[5])


#TUPLE MANIPULATION
fruits = ("apple", "banana", "cherry")
#add grape into fruits
# fruits.append("grape") #will return eror
print(type(fruits))
#convert to list first
fruits_list = list(fruits)
fruits_list.append("grape")
print(fruits_list)
fruits = tuple(fruits_list)
print(fruits)

