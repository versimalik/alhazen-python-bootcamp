#list item is stored in square bracket
numbers = [0,1,2,3,4,5,6,7,8,9]
print(type(numbers)) #mencetak tipe data
print(len(numbers)) #mencetak panjang list

fruits = ["apple", "banana", "grape"]
print(fruits)
print(type(fruits))
print(len(fruits))




#list item is stored in square bracket
numbers = [1,2,3,4,5,6,7,8,9]
#access item by calling item index
#index is started form 0, NOT from 1
print(numbers[5], numbers[6])
fruits = ["apple", "banana", "grape"]
print(fruits[1])




#list item is stored in square bracket
numbers = [0,1,2,3,4,5,6,7,8,9]
#add 10 into numbers
numbers.append(10)
print(numbers)
#change 8 into 11
numbers[8] = 11
print(numbers)
#remove 0 from numbers
numbers.remove(0)
print(numbers)
#clear all item in numbers
numbers.clear()
print(numbers)

fruits = ["apple", "banana", "grape"]
#tambahkan buah kiwi
fruits.append("kiwi")
print(fruits)
#tambahkan di awal
fruits.insert(2, "strawberry")
print(fruits)
#ubah banana menjadi pisang
fruits[1] = "pisang"
print(fruits)
#hapus grape
fruits.remove("grape")
print(fruits)
#clear all/ hapus semua
fruits.clear()
print(fruits)


#LIST CONSTRUCTOR
#creating list from ecommerce name
ecommerce = list(("shopee", "tokopedia", "lazada"))
print(ecommerce)
#creating list from string
fruits = "banana"
print(type(fruits))
spell = list(fruits)
print(spell)
#buat list dari string
text = "Congratulation"
print(type(text))
huruf = list(text)
print(huruf)
print(type(huruf))