# Raden Roro Deandriana Hanakirana Tritomo

def pangkat_rekursif(basis, pangkat):
    if pangkat == 0:
        return 1
    elif pangkat > 0:
        return basis * pangkat_rekursif(basis, pangkat - 1)
    else:
        return 1 / pangkat_rekursif(basis, -pangkat)

while True:
    print("Ini merupakan program pemangkatan negatif dan positif, tekan enter untuk berhenti")
    inp_angka = input("Masukkan Angka: ")
    if inp_angka == "":
        print("Program Selesai")
        break
    
    basis = float(inp_angka)
    inp_pangkat = input("Masukkan Pangkatan: ")
    if inp_pangkat == "":
        print("Program Selesai")
        break
    pangkat = int(inp_pangkat)
    
    hasil = pangkat_rekursif(basis, pangkat)
    print(f"Hasilnya adalah: {hasil}\n")
