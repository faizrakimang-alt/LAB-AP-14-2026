jarak_pengiriman = int(input("Masukkan jarak pengiriman (km): "))
layanan_express = str(input ("Masukkan layanan express (ya/tidak): ")).lower()

if jarak_pengiriman < 5:
    jarak = 10000
elif 5 < jarak_pengiriman <= 20:
    jarak = 20000
else:
    jarak = 35000

layanan = 15000 if layanan_express == "ya" else 0
tarif = jarak + layanan
print("Total tarif pengiriman: Rp", tarif)

