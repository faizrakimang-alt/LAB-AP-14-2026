tujuan = input("Masukkan tujuan (Pantai/Pegunungan/Kota): ").capitalize()
if tujuan not in ["Pantai", "Pegunungan", "Kota"]:
    print("Error: Tujuan tidak valid!")
    exit()
waktu = input("Masukkan waktu (Pagi/Malam): ").capitalize()
if waktu not in ["Pagi", "Malam"]:
    print("Error: Waktu tidak valid!")
    exit()
tipe = input("Masukkan tipe pengunjung (Anak/Dewasa): ").capitalize()
if tipe not in ["Anak", "Dewasa"]:
    print("Error: Tipe pengunjung tidak valid!")
    exit()


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
