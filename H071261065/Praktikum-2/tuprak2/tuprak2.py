
""""
Tugas Praktikum 2
Conditional Statements
"""

#1. Klasifikasi Tingkat Kepedasan

level_pedas = int(input("Masukkan level cabai: "))

if level_pedas < 0:
    print("Input tidak valid")
elif level_pedas <= 10:
    print("Level Aman")
elif level_pedas <= 40:
    print("Level Sedang")
elif level_pedas <= 70:
    print("Level Pedas")
else:
    print("Level Ekstrem")


#2. Tarif Pengiriman

jarak = int(input("Masukkan jarak pengiriman (km): "))
express = input("Layanan express (ya/tidak): ")

if jarak < 5:
    tarif = 10000
elif jarak >= 5 and jarak <= 20:
    tarif = 20000
else:
    tarif = 35000

if express == "ya":
    tarif += 15000

print(f"Total tarif pengiriman: Rp{tarif}")


#3. Seleksi Pelamar

nilai = int(input("Masukkan nilai tes: "))
pengalaman = int(input("Masukkan pengalaman kerja (tahun): "))

if nilai >= 80:
    print("Lolos ke Tahap Wawancara")
elif nilai >= 65 and pengalaman >= 2:
    print("Lolos Bersyarat")
else:
    print("Tidak Lolos")


#4. Rekomendasi Wisata

tujuan = input("Masukkan tujuan (Pantai/Pegunungan/Kota): ")
waktu = input("Masukkan waktu (Pagi/Malam): ")
tipe = input("Masukkan tipe pengunjung (Anak/Dewasa): ")

match tujuan:
    case "Pantai":
        if waktu == "Pagi":
            print("Paket Rekomendasi: Paket A")
        elif waktu == "Malam" and tipe == "Dewasa":
            print("Paket Rekomendasi: Paket C")
        else:
            print("Tidak ada paket yang cocok")

    case "Pegunungan":
        if waktu == "Pagi" and tipe == "Dewasa":
            print("Paket Rekomendasi: Paket B")
        elif waktu == "Malam" and tipe == "Dewasa":
            print("Paket Rekomendasi: Paket C")
        else:
            print("Tidak ada paket yang cocok")

    case "Kota":
        if waktu == "Malam":
            print("Paket Rekomendasi: Paket C")
        else:
            print("Tidak ada paket yang cocok")

    case _:
        print("Tidak ada paket yang cocok")