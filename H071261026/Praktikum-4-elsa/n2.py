def hitung_nilai(*nilai):
    rata = sum(nilai) / len(nilai)
    tertinggi = max(nilai)
    terendah = min(nilai)

    return rata, tertinggi, terendah


nilai_siswa = []

while True:
    nilai = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")

    if nilai == "":
        break

    nilai_siswa.append(float(nilai))


if len(nilai_siswa) == 0:
    print("Data nilai tidak tersedia.")
else:
    rata, tertinggi, terendah = hitung_nilai(*nilai_siswa)

    print(f"Rata-rata kelas: {rata}")
    print(f"Nilai tertinggi: {tertinggi:g}")
    print(f"Nilai terendah: {terendah:g}")