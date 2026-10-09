"""
Buat program pemesanan minuman menggunakan match case.

Pilihan minuman:

* 1 → Kopi
* 2 → Teh
* 3 → Jus
* Selain itu → Menu tidak tersedia

Setelah memilih minuman, gunakan if-else untuk mengecek ukuran:

* besar → Tambahkan Rp5.000
* Selain itu → Tidak ada tambahan

output :
Pilih minuman (1/2/3): 2
Ukuran (besar/kecil): besar

Pesanan: Teh
Total tambahan: Rp5000

"""

minuman = int(input("Pilih minuman (1/2/3): "))

match minuman:
	case 1:
		pesanan = "Kopi"
	case 2:
		pesanan = "Teh"
	case 3:
		pesanan = "Jus"
	case _:
		pesanan = "Menu tidak tersedia"

ukuran = input("Ukuran (besar/kecil): ").lower()

if ukuran == "besar":
	tambahan = 5000
else:
	tambahan = 0

print(f"Pesanan: {pesanan}")
print(f"Total tambahan: Rp{tambahan}")