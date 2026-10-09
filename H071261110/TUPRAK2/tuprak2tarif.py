#Soal 2
jarak = float(input("Masukkan jarak pengiriman: "))
express = input("Layanan express (ya/tidak): ").lower()

if jarak < 5:
    jarak = 10000
elif jarak <= 20:
    jarak = 20000
else:
    jarak = 35000

layanan = 15000 if express == "ya" else 0
tarif = jarak + layanan  
print ("total tarif pengiriman: Rp", tarif)