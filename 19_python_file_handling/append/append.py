text = "Selamat datang di kelas Python"

file = open('filebaru.txt', 'a')

file.write(text)
file.write('\n')

file.close()