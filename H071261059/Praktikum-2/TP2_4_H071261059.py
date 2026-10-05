tujuan = input("Masukkan tujuan (Pantai/Pegunungan/Kota): ").lower()
waktu = input("Masukkan waktu (Pagi/Malam): ").lower()
tipe = input("Masukkan tipe pengunjung (Anak/Dewasa): ").lower()

match tujuan:
    case "pantai":
        if waktu == "pagi":
            print("Paket rekomendasi: Paket A")
        elif waktu == "malam" and tipe == "dewasa":
            print ("Paket rekomendasi: Paket C")
        else: 
            print ("Tidak ada paket yang cocok")
        
    case "pegunungan":
        if waktu == "pagi" and tipe == "dewasa":
            print ("Paket rekomendasi: Paket B")
        elif waktu == "malam" and tipe == "dewasa":
            print ("Paket rekomendasi: Paket C")
        else:
            print ("Tidak ada paket yang cocok")

    case "kota":
        if waktu == "malam":
            print("Paket rekomendasi: Paket C")
        else:
            print ("Tidak ada paket yang cocok")
    
    case _: 
        print("Tidak ada paket yang cocok")


            



    