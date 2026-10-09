# Fungsi mencari seluruh indeks kemunculan kata dengan perulangan while dan find()
def cek_kata(teks, kata):
    indeks_list = []
    start = 0
    t_lower = teks.lower()
    k_lower = kata.lower()
    
    while True:
        pos = t_lower.find(k_lower, start)
        if pos == -1:
            break
        indeks_list.append(pos)
        start = pos + 1
    return indeks_list

# Fungsi mengecek batas kata tanpa menggunakan isalpha()
def cek_batas_kata(teks, i, panjang):
    alfabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    # Cek karakter sebelum kata
    if i > 0 and teks[i - 1] in alfabet:
        return False
        
    # Cek karakter sesudah kata
    if i + panjang < len(teks) and teks[i + panjang] in alfabet:
        return False
        
    return True

# Fungsi utama menyensor kata utuh (dengan warna merah)
def sensor_kata(teks, kata, simbol):
    posisi = cek_kata(teks, kata)
    posisi_valid = [p for p in posisi if cek_batas_kata(teks, p, len(kata))]
    teks_tersensor = ""
    i = 0
    # Merakit ulang teks secara manual
    while i < len(teks):
        if i in posisi_valid:
            # Menambahkan simbol sensor yang dibungkus kode warna merah
            teks_tersensor += + (simbol * len(kata))
            i += len(kata)
        else:
            teks_tersensor += teks[i]
            i += 1
            
    return (teks_tersensor, len(posisi_valid), posisi_valid)

# Program Utama
input_teks = input("Masukkan Teks: ")
target_kata = input("Masukkan kata target: ")
simbol_sensor = input("Masukkan simbol: ")

hasil_teks, jumlah, list_idx = sensor_kata(input_teks, target_kata, simbol_sensor)

print(f"Hasil Teks: {hasil_teks}")
print(f"Jumlah: {jumlah}  Indeks: {list_idx}")