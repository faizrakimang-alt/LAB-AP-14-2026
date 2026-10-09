ALFABET = "abcdefghijklmnopqrstuvwxyz"

def cek_sandi(ch, k):
    if ch.lower() in ALFABET:
        idx = ALFABET.find(ch.lower())
        huruf_baru = ALFABET[(idx + k) % 26]
        return huruf_baru.upper() if ch.isupper() else huruf_baru
    return ch

def mesin_enkripsi(teks, k):
    return "".join(cek_sandi(c, k) for c in teks)

def mesin_dekripsi(teks, k):
    return mesin_enkripsi(teks, -k)

def retas_sandi(sandi, kata_kunci):
    hasil = []
    for k in range(26):
        pesan = mesin_dekripsi(sandi, k)
        if kata_kunci.lower() in pesan.lower():
            hasil.append((k, pesan))
    return hasil

sandi = input("Masukkan pesan tersita (enkripsi Caesar): ")
kunci = input("Masukkan kata kunci target: ")
print(f"Output Deskripsi: {retas_sandi(sandi, kunci)}")