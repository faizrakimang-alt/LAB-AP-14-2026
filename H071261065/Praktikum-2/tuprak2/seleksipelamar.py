# 3. Seleksi Pelamar

nilai = int(input("Masukkan nilai tes (0-100): "))
pengalaman = int(input("Masukkan pengalaman kerja (tahun): "))

if nilai < 0 or nilai > 100:
    print("Nilai tes harus berada antara 0 sampai 100.")
elif pengalaman < 0:
    print("Pengalaman kerja tidak boleh negatif.")
else:
    if nilai >= 80:
        print("Lolos ke Tahap Wawancara")
    elif nilai >= 65 and pengalaman >= 2:
        print("Lolos Bersyarat")
    else:
        print("Tidak Lolos")