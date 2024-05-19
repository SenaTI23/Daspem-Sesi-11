def hitung_kata(kalimat):
  return len(kalimat.strip().split())
  
kalimat = input("kalimat :")
jumlah_kata = hitung_kata(kalimat)
print("jumlah katanya :",jumlah_kata)
