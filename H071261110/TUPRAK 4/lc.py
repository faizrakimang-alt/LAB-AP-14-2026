def faktorial(n):
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i

    return hasil

angka = int(input("Masukkan angka untuk menghitung faktorial: "))
if angka < 0:
    print("Faktorial tidak boleh angka negatif.")

print(f"Faktorial dari {angka} adalah: {faktorial(angka)}")