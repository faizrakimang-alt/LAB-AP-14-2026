nilai = float(input("Masukkan nilai tes: "))

if 100 >= nilai >=  80:
    print("Lolos ke Tahap Wawancara")

elif nilai >= 65:
    pengalaman_kerja = float(input("Masukkan pengalamana kerja (tahun) "))
    if pengalaman_kerja >= 2:
            print("Lolos bersyarat")
    else:
            print("Tidak lolos")
else: 
    print("Tidak lolos")