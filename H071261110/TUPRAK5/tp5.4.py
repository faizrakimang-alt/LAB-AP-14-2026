daftar_email_terdaftar = []

def deteksi_anomali_email(email):
    anomali = []
    
    if " " in email:
        anomali.append("Tidak boleh mengandung spasi di posisi manapun.")
        
    if email.count('@') != 1:
        anomali.append("Harus memiliki tepat satu karakter @.")
    else:
        local, domain = email.split('@')
        
        if not local or not domain:
            anomali.append("Bagian sebelum @ (local) atau setelah @ (domain) tidak boleh kosong.")
            
        if local.startswith('.') or local.endswith('.'):
            anomali.append("Bagian local tidak boleh diawali atau diakhiri titik (.).")
        if ".." in local:
            anomali.append("Bagian local tidak boleh mengandung titik berurutan (..).")
            
        if "." not in domain:
            anomali.append("Bagian domain wajib memiliki minimal satu titik.")
        if ".." in domain or domain.endswith('.'):
            anomali.append("Bagian domain tidak boleh mengandung titik berurutan atau diakhiri titik.")

        if not (domain.endswith('.com') or domain.endswith('.id') or domain.endswith('.ac.id')):
            anomali.append("Wajib berakhiran dengan .com, .id, atau .ac.id")

    if email in daftar_email_terdaftar:
        anomali.append("Email sudah terdaftar (Duplikat).")
        
    return anomali

def cetak_daftar(daftar_email_valid, karakter_border):
    if not daftar_email_valid:
        return
        
    max_len = max(len(e) for e in daftar_email_valid)
    border = karakter_border * (max_len + 6)
    
    print("\n" + border)
    print(f"{karakter_border} HASIL EMAIL VALID {karakter_border}")
    print(border)
    for email in daftar_email_valid:
        print(f"| {email.ljust(max_len)} |")
    print(border)

print("--- Sistem Pencatatan email valid ---")
border_char = input("Masukkan border dengan karakter bebas: ").strip() or "="
print("Ketik 'tutup' untuk mengakhiri masukan dan mencetak email.\n")

daftar_valid = []
while True:
    e = input("Masukkan email: ").strip()
    if e.lower() == 'tutup':
        break
        
    err = deteksi_anomali_email(e)
    if not err:
        print(">> Email VALID!")
        daftar_valid.append(e)
        daftar_email_terdaftar.append(e)
    else:
        print(">> Email DITOLAK karena:")
        for pesan in err:
            print(f"   {pesan}")

cetak_daftar(daftar_valid, border_char)