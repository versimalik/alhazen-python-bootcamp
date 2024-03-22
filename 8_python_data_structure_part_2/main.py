#PROJECT
# Meminta pengguna untuk memasukkan nilai untuk hobby
name = input("Masukkan nama hobby favorit: ")
function = input("Masukkan fungsi hobby favorit: ")

# Membuat dictionary menggunakan dict() function
hobby_dict = dict(name=name, function=function)

# Mencetak dictionary
print("Dictionary awal:")
hobby_dict["waktu"] = "per minggu"
hobby_dict.pop("year", 2021)
print(hobby_dict)




# # Menambahkan kunci dan nilai baru ke dalam dictionary
# hobby_dict["keys"] = "value"
# hobby_dict.pop("year", None)  # Menghapus kunci "year" jika ada
# hobby_dict.pop("place", None)  # Menghapus kunci "place" jika ada

# # Mencetak dictionary setelah dimodifikasi
# print("\nDictionary setelah dimodifikasi:")
# print(hobby_dict)
