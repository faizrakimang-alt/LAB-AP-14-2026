def konversi(suhu, asal, tujuan):

    if asal not in ["C", "F", "K"] or tujuan not in ["C", "F", "K"]:
        raise ValueError

    if asal == tujuan:
        return suhu

    if asal == "C" and tujuan == "F":
        return suhu * 9 / 5 + 32

    if asal == "F" and tujuan == "C":
        return (suhu - 32) * 5 / 9

    if asal == "C" and tujuan == "K":
        return suhu + 273.15

    if asal == "K" and tujuan == "C":
        return suhu - 273.15


print("=== Konversi Suhu ===")

while True:
    try:
        suhu = input("Masukkan suhu (atau 'selesai' untuk keluar): ")

        if suhu == "selesai":
            break

        suhu = float(suhu)

        asal = input("Skala asal (C/F/K): ").upper()
        tujuan = input("Skala tujuan (C/F/K): ").upper()

        hasil = konversi(suhu, asal, tujuan)

        print(f"Hasil: {suhu} {asal} = {hasil:.2f} {tujuan}")

    except ValueError:
        print("Error: Skala suhu tidak dikenali.")