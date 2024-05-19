def is_palindrom(kata):
  return kata.lower().replace(' ', '') == kata[::-1]

kata = input("katanya :")

if is_palindrom(kata):
  print(f"{kata} adalah palindrom")
else:
  print(f"{kata} bukan palindrom")
