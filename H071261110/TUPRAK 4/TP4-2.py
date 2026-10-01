def rekap_nilai(*args):
    if not args:
        return None
    
    rata_rata = sum(args) / len(args)
    tertinggi = max(args)
    terendah = min(args)
    
    return rata_rata, tertinggi, terendah

daftar_nilai = []

while True:
    input_str = input("Masukkan nilai ujian siswa (kosongkan untuk selesai): ")
    if input_str == "":
        break
    
    # Mengonversi nilai ke int jika bulat, atau float jika desimal
    nilai = float(input_str)
    if nilai.is_integer():
        nilai = int(nilai)
    
    daftar_nilai.append(nilai)

if daftar_nilai:
    rata, tertinggi, terendah = rekap_nilai(*daftar_nilai)
    print(f"Rata-rata kelas: {rata}")
    print(f"Nilai tertinggi: {tertinggi}")
    print(f"Nilai terendah: {terendah}")
else:
    print("Data nilai tidak tersedia.")