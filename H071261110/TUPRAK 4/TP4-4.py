def konversi_suhu(suhu, skala_asal, skala_tujuan):
    skala_valid = ['C', 'F', 'K']
    skala_asal = skala_asal.upper()
    skala_tujuan = skala_tujuan.upper()

    # Validasi skala menggunakan raise Exception
    if skala_asal not in skala_valid or skala_tujuan not in skala_valid:
        raise ValueError("Skala suhu tidak dikenali.")

    # Konversi dari skala asal ke Celsius
    if skala_asal == 'C':
        celsius = suhu
    elif skala_asal == 'F':
        celsius = (suhu - 32) * 5/9
    elif skala_asal == 'K':
        celsius = suhu - 273.15

    # Konversi dari Celsius ke skala tujuan
    if skala_tujuan == 'C':
        return celsius
    elif skala_tujuan == 'F':
        return (celsius * 9/5) + 32
    elif skala_tujuan == 'K':
        return celsius + 273.15

print("=== Konversi Suhu ===")

while True:
    input_suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ").strip()
    if input_suhu.lower() == 'selesai':
        break

    try:
        suhu = float(input_suhu)
        skala_asal = input("Skala asal (C/F/K): ").strip()
        skala_tujuan = input("Skala tujuan (C/F/K): ").strip()

        # Pemanggilan fungsi dengan penanganan error
        hasil = konversi_suhu(suhu, skala_asal, skala_tujuan)
        print(f"Hasil: {suhu:.1f} {skala_asal.upper()} = {hasil:.1f} {skala_tujuan.upper()}")

    except ValueError as e:
        if str(e) == "Skala suhu tidak dikenali.":
            print(f"Error: {e}")
        else:
            print("Error: Masukkan angka suhu yang valid.")