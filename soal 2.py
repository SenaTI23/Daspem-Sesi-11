def jumlah_daftar(daftar):
  total = 0
  for angka in daftar:
    total += angka
  return total


my_list = [1, 2, 3, 4, 5]
hasil_jumlah = jumlah_daftar(my_list)
print("hasil akhir :",hasil_jumlah)
