persentase_cabai= int(input("Masukkan persentase cabai: "))
if 0 <= persentase_cabai <= 10:
    print("Level Aman")
elif 10 < persentase_cabai <=40:
    print("Level Sedang")
elif 40 < persentase_cabai <= 70:
    print("Level Pedas")
elif 70 < persentase_cabai:
    print("Level Ekstrem")
else:
    print("Input Tidak Valid")