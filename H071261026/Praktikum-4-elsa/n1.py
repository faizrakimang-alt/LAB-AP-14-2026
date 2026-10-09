print("Selamat datang di Kasir Minimarket!")

def hitung_subtotal(harga, jumlah, member=False):
    subtotal = harga * jumlah

    if member:
        subtotal = subtotal * 0.9

    return subtotal


member = input("Apakah Anda member? (y/n): ")

total = 0

while True:
    nama_barang = input("Masukkan nama barang (kosongkan untuk selesai): ")
        
    if nama_barang == "":
        break


    harga = int(input("Harga barang: "))
    jumlah = int(input("Jumlah barang: "))
    
    
    subtotal = hitung_subtotal(harga, jumlah, member == "y")

    print(f"Subtotal {nama_barang}: Rp{subtotal}")

    total = total + subtotal

print(f"Total belanja: Rp{total}")