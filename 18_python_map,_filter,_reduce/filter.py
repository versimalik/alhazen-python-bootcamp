# def even_numbers(numbers):
#     even_list = []
#     for n in numbers:
#         if n % 2 == 0:
#             even_list.append(n)
#     return even_list

# print(even_numbers(range(1, 101)))

numbers = range(1,201)

def is_even(number):
    return number % 2 == 0

even_numbers = filter(is_even, numbers)
print(list(even_numbers))

odd_numbers = filter(lambda n : n % 2 == 1, numbers)
print(list(odd_numbers))