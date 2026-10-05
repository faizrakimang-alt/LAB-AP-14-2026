jarak_pengiriman = float(input("Masukkan jarak pengiriman (km): "))
if jarak_pengiriman <= 0:
    print("Input tidak valid")

else:
    express = input("Layanan Express (ya/tidak): ").lower()
    if 0 < jarak_pengiriman < 5:
        tarif = 10000
    elif 5 <= jarak_pengiriman <= 20:
        tarif = 20000
    else: 
        tarif = 35000
    tambahan = 15000 if express == "ya" else 0
    total = tarif + tambahan
    print(f"Total tarif pengiriman: Rp{total} ")