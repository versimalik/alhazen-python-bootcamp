def average(*args):
    result = 0
    text = ""

    for num in args:
        result += num
        
    print(result/len(args))

average(1, 2, 3, 4, 5)
