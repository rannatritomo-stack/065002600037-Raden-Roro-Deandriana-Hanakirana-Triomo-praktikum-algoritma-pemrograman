total_harga = 0

while True:
    masuk_umur = input("masukkan umur: ")
    if masuk_umur == "":
        break
    
    umur = int(masuk_umur)
    
    if umur <= 2:
        harga = 0.00
        print("Gratis")
    elif 3 <= umur <= 12:
        harga = 14.00
        print(f"Harga ${harga:.2f}")
    elif umur >= 65:
        harga = 18.00
        print(f"Harga ${harga:.2f}")
    else:
        harga = 23.00
        print(f"Harga ${harga:.2f}")
        
    total_harga += harga
    print(f"Running total: {total_harga:.2f}")

print(f"masukkan umur:")
masuk_uang = float(input("masukkan jumlah uang: "))
kembalian = masuk_uang - total_harga

print(f"Running kembalian: {kembalian:.2f}")
