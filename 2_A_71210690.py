print("############################")
print("Kalkulator Advance Sederhana")
print("############################")
print("1. Menghitung sisa hasil bagi ")
print("2. Membulatkan ke bawah hasil pembagian")
print("3. Mencari akar kubik sebuah bilangan")
pilihan=int(input("Masukkan menu yang anda pilih: "))
if(pilihan==1):
    b1=float(input("Masukkan bilangan yang ingin dibagi: "))
    b2=float(input("Masukkan bilangan pembagi: "))
    hasil=b1%b2
    print("Sisa hasil bagi",b1,"dibagi dengan",b2,"adalah",hasil)
elif(pilihan==2):
    b1=float(input("Masukkan bilangan yang ingin dibagi: "))
    b2=float(input("Masukkan bilangan pembagi: "))
    hasil=b1/b2
    print("Hasil pembagian",b1,"dibagi dengan",b2,"dibulatkan kebawah adalah",hasil)
elif(pilihan==3):
    b1=float(input("Masukkan bilangan yang ingin dicari akar kubiknya: "))
    hasil=b1**(1/3)
    print("Akar kubik dari",b1,"adalah",hasil)
else:
    print("Menu yang anda pilih tidak tersedia")




