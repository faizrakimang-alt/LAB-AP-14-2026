def hitung_subtotal(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah
    if adalah_member:
        subtotal *= 0.9
    return int(subtotal)

print("Selamat datang di Kasir Minimarket!")
status_member = input("Apakah Anda member? (y/n): ").strip().lower()
is_member = status_member == 'y'

total_belanja = 0

while True:
    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")
    if nama_barang == "":
        break
    
    harga_barang = int(input("Harga barang: "))
    jumlah_barang = int(input("Jumlah barang: "))
    
    subtotal = hitung_subtotal(harga_barang, jumlah_barang, adalah_member=is_member)
    total_belanja += subtotal
    
    print(f"Subtotal {nama_barang}: Rp{subtotal}")

print(f"Total belanja: Rp{total_belanja}")