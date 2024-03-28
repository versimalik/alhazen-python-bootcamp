try:
    file = open('newfile.txt', 'r')
    print(file.read()) 
except FileNotFoundError:
    print("File yang dimaksud tidak ada!")