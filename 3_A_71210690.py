pilihan=(input("Mendatar/Menurun?: "))
jumlah=int(input("Masukkan kolom: "))
if pilihan=="Mendatar":
        print("#"*jumlah)
elif pilihan=="Menurun":
        print("*\n"*jumlah)
else:
    print("Pola tidak dikenali")
    
