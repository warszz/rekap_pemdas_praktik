#oprator and
A=bool(int(input("masukan nilai A (0/1):")))
B=bool(int(input("masukan nilai B (0/1):")))
print("A and B :", A and B)

#oprator or
A=bool(int(input("masukan nilai A (0/1):")))
B=bool(int(input("masukan nilai B (0/1):")))
print("A or B :", A or B)

#oprator not
A=bool(int(input("masukan nilai A (0/1):")))
B=bool(int(input("masukan nilai B (0/1):")))
print("not A:", not A)
print("not B:", not B)

#latihan 1
usia=int(input("masukan umur"))
cek = (usia >=18)
print(f'apakah tergolong dewasa {cek}')

#latihan 2
angka = int(input("masukan angka"))

if angka > 0 :
    print("angka positif ")
else:
    print("angka negatif")

if angka %2==0:
    print("dan angka genap")
else:
    print("dan angka ganjil")
