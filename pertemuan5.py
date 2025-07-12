usia =int(input("masukan umur"))
if usia > 20:
    print("dewasa")
elif usia > 10:
    print("remaja")
else:
   print("anak anak")


# latihan 2

nilai = int(input("masukan nilai: "))
if nilai > 90:
    print("selamat anda mendapakan  A")
elif nilai > 30:
    print("dapat  B")
else:
    print("tingkat kan lagi anda mendapatkan c")


# latihan 3

angka = int(input("Masukkan sebuah angka: "))  

match angka:
    case 0:
        print("Angka tersebut adalah NOL.")
    case b if b > 0:
        print("Angka tersebut POSITIF.")
    case a if a < 0:
        print("Angka tersebut NEGATIF.")
