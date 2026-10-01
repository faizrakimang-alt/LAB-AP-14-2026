def hitung_mundur(angka):
    print(angka)
    if angka == 0:
        print("luncurkan")
    else:
        hitung_mundur(angka -2)

while True:
    angka_awal = int(input("masukkan angka awal hitung mundur: "))

    if angka_awal < 0:
        print("input tidak valid, angka tidak boleh negatif. ")
    else:
        break

hitung_mundur(angka_awal)