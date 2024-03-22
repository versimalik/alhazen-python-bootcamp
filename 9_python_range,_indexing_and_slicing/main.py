#PROJECT
#case = numbers slicer
#file:number-slicer.py

# create a variable called 'numbers'
numbers = list(range(1,251))
# creat a list of numbers 1 - 250 using list(range())

# print a number from index 15
print(numbers[15])

# print an eight number from the back
# clue : negative indexing
print(numbers[-8])


# print a group of numbers, start from 55 until 67
print(numbers[54:67])



# print a group of even numbers, starts from 70 until 240
# clue : use step parameter

print(numbers[69 :241  : 2])