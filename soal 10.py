def is_anagram(kata1, kata2):
  return sorted(kata1.lower()) == sorted(kata2.lower())
  
kata1 = input("kata pertama :")
kata2 = input("kata kedua :")

if is_anagram(kata1, kata2):
  print(f"{kata1} dan {kata2} adalah True.")
else:
  print(f"{kata1} dan {kata2} bukan False.")
