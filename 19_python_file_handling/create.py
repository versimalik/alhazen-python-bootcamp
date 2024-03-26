try:
    open('newfile.txt', 'x')
except FileExistsError:
    print("File sudah ada! Tidak bisa dibuat lagi")