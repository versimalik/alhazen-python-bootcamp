import time

def countdown(number):
    print(number)
    time.sleep(1)
    if number != 0:
        countdown(number - 1)

countdown(10)