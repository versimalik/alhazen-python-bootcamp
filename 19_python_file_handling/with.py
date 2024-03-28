with open('biodata.txt', 'a') as file:
    file.write('Ini adalah biodata saya')

read_file = open('biodata.txt', 'r')
print(read_file.read())