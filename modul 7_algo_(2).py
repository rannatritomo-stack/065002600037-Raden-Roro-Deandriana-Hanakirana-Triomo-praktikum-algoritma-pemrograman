# Raden Roro Deandriana Hanakirana Tritomo

def tentukan_ordinal(angka):
    if 11 <= angka % 100 <= 13:
        suffix = 'th'
    else:
        s = angka % 10
        if s == 1:
            suffix = 'st'
        elif s == 2:
            suffix = 'nd'
        elif s == 3:
            suffix = 'rd'
        else:
            suffix = 'th'
    return (angka, suffix)

# Program Utama
print("Ordinal Number")
print("ketik 0 untuk menghentikan program")

while True:
    angka = int(input("masukkan angka: "))
    if angka == 0:
        print((0, 'th'))
        print("terima kasih telah menggunakan program saya")
        break
    
    hasil = tentukan_ordinal(angka)
    print(hasil)
