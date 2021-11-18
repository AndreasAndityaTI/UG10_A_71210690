artikel = input("Masukkan artikel yang ingin dipindai: ")
nama_klub = input("Masukkan nama klub favorit Anda: ")
score = input("Masukkan score yang ingin dicari: ")
if (score and nama_klub) in artikel:
	print("Hasil pencarian ditemukan")
elif score in artikel:
	print("Hanya skor {} yang ditemukan pada artikel ini".format(score))
elif nama_klub in artikel:
	print("Hanya kata {} yang ditemukan pada artikel ini".format(nama_klub))
else:
	print("Hasil pencarian {} dan {} tidak ditemukan".format(nama_klub,score))