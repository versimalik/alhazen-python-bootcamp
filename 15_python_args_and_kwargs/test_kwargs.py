# def calculate(*args, **kwargs):
#     ops = kwargs.values()
#     print(args)
#     print(kwargs)
#     for op in ops:
#         if op == "+":
#             result = 0
#             for n in args:
#                 result += n
#                 print(result)
#         elif op == "-":
#             result = 0
#             for n in args:
#                 result -= n
#                 print(result)

# calculate(1, 2, 3, 4, 5, add = "+", substract = "-")

def wordloop(*args, **kwargs):
    txts = kwargs.values()
    for i in args:
        print(i, "".join(txts))

wordloop(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "11", text = "Hello")