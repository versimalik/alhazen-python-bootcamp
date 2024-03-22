awal = input("Masukkan nilai awal: ")
akhir = input("Masukkan nilai akhir: ")

choice = input("even atau odd? ")

if choice == 'even':
    for i in range(int(awal), int(akhir)+1):
        if i % 2 == 0:
            print(i)
elif choice == 'odd':
     for i in range(int(awal), int(akhir)+1):
        if i % 2 != 0:
            print(i)