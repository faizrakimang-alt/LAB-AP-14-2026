nilai_tes = int(input("Masukkan nilai tes: "))

if nilai_tes >= 80:
    print ("Lolos ke tahap wawancara")
else:
    pengalaman = int(input("Masukkan pengalaman kerja (tahun): "))

    if (65 <= nilai_tes < 80) and pengalaman >= 2:
        print("Lolos Bersyarat")
    else:
        print("Tidak Lolos")