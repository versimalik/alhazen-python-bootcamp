# def addition(a,b):
#     add = a + b
#     result = f"{a} + {b} = {add}"
#     print(result)

def addition(*nums):
    result = 0
    for i in nums:
        result += i
    print(result)

addition(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
