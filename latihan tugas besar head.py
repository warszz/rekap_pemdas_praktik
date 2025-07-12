import p

saldo = 2000000  
while True:
    menu = int(input("Pilih menu (1: top up, 2: keluar): "))
    if menu == 1:
        saldo =p.top_up(saldo)  
    elif menu == 2:
        break
    else:
        print("Menu tidak valid.")