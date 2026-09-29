print("=== Program Kasir Otomatis Dinas Store ===") 
print("Ketik `0`untuk menutup toko dam mengakhiri sesi.")

while True:
    try:
      item = input("Masukkan jumlah item: ")
      item = int(item)

      if item == 0:
         print("Toko ditutup. Sesi rekap selesai.")
         break
      elif item < 0:
         print("Jumlah tidak boleh negatif")
         continue
      elif item > 100:
         print("Maksimal 100 item per transaksi!")
      else:
         print(f"Transaksi {item} item berhasil!") 
        
    except ValueError:
     print("Input harus berupa angka!")