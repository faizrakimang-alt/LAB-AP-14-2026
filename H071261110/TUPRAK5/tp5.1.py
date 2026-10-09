def bersihkan_teks(teks):
    teks_bersih = ""
    for char in teks:
        if char.lower() in "abcdefghijklmnopqrstuvwxyz":
            teks_bersih += char.lower()
    return teks_bersih

def cek_palinrome(teks):
    teks_balik = "".join(reversed(teks))
    if teks == teks_balik:
        return (True, -1)
    for i in range(len(teks)):
        if teks[i] != teks_balik[i]:
            return (False, i)

def inti_palinrome(teks):
    teks_b = bersihkan_teks(teks)
    n = len(teks_b)
    pal_terpanjang = ""
    idx_awal = 0
    max_len = 0

    for i in range(n):
        for j in range(i + 1, n + 1):
            sub = teks_b[i:j]
            is_palin, _ = cek_palinrome(sub)
            if is_palin and len(sub) > max_len:
                max_len = len(sub)
                pal_terpanjang = sub
                idx_awal = i

    return {"teks": pal_terpanjang, "panjang": max_len, "indeks_awal": idx_awal}

input_prasasti = input("Masukkan teks prasasti: ")
print(f"Teks Bersih: {bersihkan_teks(input_prasasti)}")
print(f"Output Terharap: {inti_palinrome(input_prasasti)}")