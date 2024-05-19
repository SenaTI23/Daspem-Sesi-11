def hitung_faktorial(n):
  return 1 if n == 0 else n * hitung_faktorial(n - 1)

n = int(input("parameter :"))
faktorial = hitung_faktorial(n)
print("parameternya :",n)
print("hasil :",faktorial)
