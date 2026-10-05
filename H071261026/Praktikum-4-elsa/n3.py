def peluncuran_roket(angka): 
    print(angka)
    
    if angka == 0:
        print("Luncurkan!")
    else:
        peluncuran_roket(angka - 1)
        
        
while True:
    hitungan =int(input("Masukkan angka awal hitung mundur: "))
        
    if hitungan < 0:
        print("Input tidak valid,angka tidak boleh negatif!")
    else:        
        peluncuran_roket(hitungan)
        break
            