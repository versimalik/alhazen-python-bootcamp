from functools import reduce

numbers = range(1,11)

def addition(number1, number2):
    result = number1 + number2
    return result

total = reduce(addition, numbers)
print(total)