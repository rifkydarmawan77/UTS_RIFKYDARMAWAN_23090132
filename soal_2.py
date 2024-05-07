tahun = int(input('Masukkan Tahun :'))
if tahun % 400 == 0:
 print("Tahun", tahun, "merupakan TAHUN KABISAT")
elif tahun % 4 == 0 and tahun % 100 != 0:
 print("Tahun",tahun,"merupakan TAHUN KABISAT")
else:
 print("Tahun", tahun, "BUKAN TAHUN KABISAT")