def luas_persegi (sisi):
    return sisi * sisi
hasil = luas_persegi(int(input("masukan angka! ")))
print("hasil luas persegi: ", hasil)

#latihan 2
def hitung_diskon (harga, diskon):
    potongan = harga * (diskon//100)
    harga_setelah_diskon = harga - potongan
    return harga_setelah_diskon

harga_awal= int(input("masukan harga! "))
diskon=50
harga_akhir = hitung_diskon(harga_awal, diskon)
print("harga  awal ", harga_awal)
print("diskon ", diskon, "%")
print("harga setelah diskon: ", harga_akhir)



    
    