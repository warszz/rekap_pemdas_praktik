def top_up(saldo_update):
    print("Pilih paket:\n 1. jaket - 50000\n 2. sepatu - 120000\n 3. sandal - 50000")
    
    pilihan = input("Masukkan pilihan (1/2/3): ")
    
    if pilihan == '1':
         harga = 50000
         barang = "jaket"
    elif pilihan == '2':
         harga = 120000
         barang = "sepatu"
    elif pilihan == '3':
         harga = 50000
         barang = "sendal"
    else:
        print("Pilihan tidak valid.")
        return saldo_update  

    if saldo_update >= harga:
        saldo_update -= harga
        print(f"Anda telah membeli paket {barang}. Sisa saldo: {saldo_update}")
    else:
        print("Saldo tidak cukup untuk membeli barang ini.")
    
    return saldo_update  




    
    
    