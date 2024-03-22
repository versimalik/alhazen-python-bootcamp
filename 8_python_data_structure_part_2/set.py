#set item is stored in curly bracket
#unordered
#do not allow duplicate values
#unchangeable
#access set item set item cannot be accessed by callinng its index
numbers = {0,5,4,8,2,7,2}
#set items will be displayed unordered
print(numbers)
print(type(numbers))
print(len(numbers))
#duplicated item will be ignored in set
fruits = {"banana", "apple", "manggo", "apple"}
print(fruits)


#SET ITEM
cars = {"honda", "volvo", "toyota"}
#this command will return eror
# print(cars[1])
#using for loop
# for i in cars:
#   print(i)
for car in cars:
    print(car)
    break

fruits = {"banana", "apple", "manggo", "apple"}
for fruit in fruits:
  print(fruit)
  break


#SET MANIPULATION
#bcs set item cannot accessed by its index
#it is also cannot be changed
names = {"andi", "abby", "andi", "salma"}
# names[0] = "adit"
names.add("adit")
print(names)
names.discard("syifa") #if item is not found, it will not return eror
print(names)
names.remove("syifa") # if item is not found, it will return eror
print(names)
names.pop()
print(names) # remove random

fruits = {"banana", "apple", "manggo", "apple"}
fruits.add("strawberry")
print(fruits)



#another ways to add items in existing set
names = {"andi", "abby", "andi", "benny"}
friends = {"tony", "rendy"}
friend_list = ["angel", "cindy"]
#add "friends" set into "names" set
names.update(friends)
print(names)
#add friend_list into "names" set
names.update(friend_list)
print(names)



#SET CONSTRUCTOR
#create set using set() function
cars = set(("honda", "toyota", "suzuki")) #tuple
print(type(cars))
print(cars)
#create set formm string
text = set("python")
print(type(text))
print(text)