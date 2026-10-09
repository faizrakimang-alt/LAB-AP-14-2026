jarak = int(input("Masukkan jarak pengiriman (km): "))
express = input("Layanan express (ya/tidak): ").capitalize()

if jarak < 5:
    tarif = 10000
elif jarak <= 20:
    tarif = 20000
else:
    tarif = 35000

tambahan = 15000 if express == "Ya"  else 0

total = tarif + tambahan

print("Total tarif pengiriman: Rp", total)
