ug=float(input("Masukkan nilai rata-rata UG anda: "))
tts=float(input("Masukkan nilai TTS anda: "))
tas=float(input("Masukkan nilai TAS anda: "))
rug=ug*(70/100)
rtts=tts*(15/100)
rtas=tas*(15/100)
total=rtts+rtas+rug
print("=========================")
print("Nilai anda: ",total)
if(total>=85):
    grade="A"
elif(total>=80):
    grade="A-"
elif(total>=75):
    grade="B+"
elif(total>=70):
    grade="B"
elif(total>=65):
    grade="B-"
elif(total>=60):
    grade="C+"
elif(total>=55):
    grade="C"
elif(total>=45):
    grade="D"
else:
    grade="E"
print("Nilai huruf anda: ",grade)

