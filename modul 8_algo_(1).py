# Raden Roro Deandriana Hanakirana Tritomo

def input_jumlah(n, i=1):
    if i > n:
        return 0
    else:
        angka = int(input(f"Masukkan angka ke-{i}: "))
        return angka + input_jumlah(n, i + 1)

jumlah = int(input("Masukkan Jumlah: "))
hasil = input_jumlah(jumlah)
print(f"Hasil dari penjumlahan adalah: {hasil}")
