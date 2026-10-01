def hitung_subtotal(harga, jumlah, adalah_member=False):
    subtotal = harga * jumlah

    if adalah_member:
        subtotal_semua = subtotal - (subtotal * 0.10)
        return subtotal_semua
    return subtotal


print("selamat datang di kasir minimarket!")

status_member = input("apakah anda member? (yes/no): ")
member = status_member.lower() == "yes"

sub_total = 0

while True:
    nama_barang = input("masukkan nama barang (kosongkan untuk selesai): ")

    if nama_barang == "":
        break

    harga = int(input("harga barang: "))
    jumlah = int(input("jumlah barang: "))

    sub_totall = hitung_subtotal(harga, jumlah)

    sub_total += sub_totall
    print(f"subtotal {nama_barang}: Rp{int(sub_total)}: ")

print(f"total_belanja: Rp{int(sub_total)}:")