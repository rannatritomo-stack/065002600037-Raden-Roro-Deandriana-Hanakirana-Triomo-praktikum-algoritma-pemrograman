def cek_faktor(angka):
    faktor = 0
    for i in range(1, angka + 1):
        if angka % i == 0:
            faktor += 1
    return faktor

def cek_prima(angka):
    if angka <= 1:
        return f"{angka} bukanlah bilangan Prima"
    
    if cek_faktor(angka) == 2:
        return f"{angka} adalah bilangan Prima"
    else:
        return f"{angka} bukanlah bilangan Prima"

# Program Utama
angka_input = int(input("Masukkan angka: "))
print(cek_prima(angka_input))
