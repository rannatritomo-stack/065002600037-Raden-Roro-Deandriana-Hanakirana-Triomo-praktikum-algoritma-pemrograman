#function call

def konversi_nilai(huruf):
    if huruf == "A":
        peringkat = 9
    elif huruf == "A-":
        peringkat = 8
    elif huruf == "B+":
        peringkat = 7
    elif huruf == "B":
        peringkat = 6
    elif huruf == "B-":
        peringkat = 5
    elif huruf == "C+":
        peringkat = 4
    elif huruf == "C":
        peringkat = 3
    elif huruf == "D":
        peringkat = 2
    elif huruf == "E":
        peringkat = 1
    else:
        peringkat = None
    return peringkat

total_nilai = 0
jumlah = 0

while True:
    masuk = input("masukkan nilai: ")
    if masuk == "":
        break
    
    huruf = masuk.strip().upper()
    hasil = konversi_nilai(huruf)
    
    if hasil is not None:
        print(f"nilai = {hasil}")
        total_nilai += hasil 
        jumlah += 1
    else:
        print("Kategori nilai tidak valid!")

if jumlah > 0:
    rata_rata = total_nilai / jumlah  
    print(f"rata - rata nya adalah: {rata_rata}")
else:
    print("Tidak ada nilai yang dimasukkan.")
