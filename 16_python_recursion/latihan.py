def factorial(number):
    if number > 0  and number < 2:
        return 1    
    elif number > 1:
        result = number * factorial(number - 1)
        return result
    else:
        return "Number must be > or = to 0!!!"
    
title = "Factorial Calculator"

print("=" * len(title))
print(title)
print("=" * len(title), end="\n\n")

number = int(input("What number to calculate factorial? "))
print(factorial(number))
