mkn = int(input("Pilih Menu (1-3): "))
ukuran = input("Pilih ukuran (Besar/kecil): ").capitalize()

match mkn:

    case 1:
        print("anda memilih kopi")

    case 2:
        print(" anda memilih Teh")

    case 3:
        print("anda memilih Jus")
    case _:
        print("bahasa tidak tersedia")

tambahan = 5000 if ukuran == "Besar" else 0
total = tambahan

print("total tambahan: Rp",total)