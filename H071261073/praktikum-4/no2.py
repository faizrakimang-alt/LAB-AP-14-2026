def rekap_nilai(*args):
    rata = sum(args) /  len(args)
    tertinggi = max(args)
    terendah = min(args)

    return rata, tertinggi, terendah

data_nilai = []
while True:
    nilai = input("masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    if nilai == "":
        break
    data_nilai.append(float(nilai))

if len(data_nilai) == 0:
    print("data nilai tidak tersedia")
else:
    rata, tinggi, rendah = rekap_nilai(*data_nilai)

    print(f"rata-rata kelas: {rata}")
    print(f"nilai tertinggi: {int(tinggi)}")
    print(f"nilai terendah: {int(rendah)}")