def factorial(number):
    if number <= 1:
        return 1    
    elif number > 1:
        result = number * factorial(number - 1)
        return result
    
print(factorial(0))