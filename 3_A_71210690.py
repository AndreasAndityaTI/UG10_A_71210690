pilihan=(input("Mendatar/Menurun?: "))
jumlah=int(input("Masukkan kolom: "))
x=1
if pilihan=="Mendatar":
        print("#"*jumlah)
elif pilihan=="Menurun":
        print("*\n"*jumlah)
else:
    print("Pola tidak dikenali")
    
