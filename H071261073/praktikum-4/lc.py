def hitung_faktorial(n):
    hasil = 1
    for i in range(1, n + 1):
        hasil *= i
    return hasil



angka =int (input("masukkan angka: "))


print(f"faktorial dari {angka} adalah {hitung_faktorial(angka)}:")



