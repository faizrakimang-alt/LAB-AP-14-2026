
def konversi(suhu, asal, tujuan):
    if asal not in "CFK" or tujuan not in "CFK":
        raise ValueError("skala tidak dikenali.")

    if asal == "F":
        suhu = (suhu - 32)
    elif asal == "K":
        suhu = suhu - 273.15

    if tujuan == "F":
        suhu = suhu * 9 / 5 + 32
    elif tujuan == "K":
        suhu = suhu + 273.15

    return suhu

print("konversi suhu")
while True:
    input_suhu = input("masukkan suhu (atau 'selesai' untuk keluar): ")

    if input_suhu.lower() == "selesai":
        break

    try:
        suhu = float(input_suhu)
        asal = input("skala asal (C/F/K): ").upper()
        tujuan = input("skala tujuan (C/F/K): ").upper()

        hasil = konversi(suhu, asal, tujuan)


        print(f"hasil: {suhu} {asal} = {hasil:.1f} {tujuan}")
    except ValueError as e:
        print("Error:", e)
