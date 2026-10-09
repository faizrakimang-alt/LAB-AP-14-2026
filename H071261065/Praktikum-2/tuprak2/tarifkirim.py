# 2. Tarif Pengiriman

jarak = int(input("Masukkan jarak pengiriman (km): "))

if jarak <= 0:
    print("Jarak tidak boleh 0 atau negatif.")
else:
    express = input("Layanan express (ya/tidak): ")

    if express != "ya" and express != "tidak":
        print("Input layanan express harus 'ya' atau 'tidak'.")

    else:
        if jarak < 5:
            tarif = 10000
        elif jarak <= 20:
            tarif = 20000
        else:
            tarif = 35000

        tarif += 15000 if express == "ya" else 0

        print(f"Total tarif pengiriman: Rp{tarif}")