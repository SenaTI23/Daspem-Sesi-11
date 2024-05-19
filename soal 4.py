def angka_unik(my_list):
  return len(set(my_list))

my_list = [1, 2, 3, 3, 4, 4, 5, 8, 10]
jumlah_unik = angka_unik(my_list)
print("jumlah elemen :",jumlah_unik)