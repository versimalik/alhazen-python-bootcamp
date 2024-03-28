import re
# import stringcolor

username = str(input("Masukkan username: "))
password = str(input("Masukkan password: "))

while not re.fullmatch(r"[A-Za-z0-9]{6,}", password):
    print("Password harus berisi: ")
    print("Huruf kecil")
    print("Huruf besar")
    print("Angka")
    print("Minimal 6 karakter")
    password = str(input("Masukkan password: "))
else:
    print("berhasil login")
