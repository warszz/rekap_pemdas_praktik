print("menu \n1. menabung \n2. cek saldo \n3. penarikan tunai \n4. transfer \n5. kirim e-wallet \n6. ubah mata uang \n7. selesai")
pin= input ("masukan pin anda: ")
if pin != "1234" :
    print("pin salah!!!!!!")
    exit()
saldo = 0
admin_1 = 12000
admin_2 = 5000
admin_3 = 2000
while True:
    menu = int(input("silahkan pilih menu (1/2/3/4/5/6): "))
    if menu == 1:
        debit = int(input("masukan jumlah saldo debit:  "))
        saldo= saldo + debit - admin_2
        print(f"sisa saldo anda {saldo}")
    elif menu == 2:
        print(f"jumlah saldo anda saat ini adalah {saldo}")
    elif menu == 3:
        kredit = int(input("masukan saldo yang ingin di tarik: ")) 
        if saldo >= 60000 and kredit <= 5000000:
            saldo = saldo -kredit
            print(f"sisa saldo anda adalah {saldo}")
        else:
            print("saldo tidak mencukupi")
    elif menu == 4:
            kredit = int(input("jumlah yang akan di kirim: "))
            if saldo >= 10000 and kredit <= 5000000:
                saldo = saldo -kredit -admin_1
                print(F"trasfer berhasil \nsisa saldo anda {saldo}")
            else:
                print("saldo anda tidak mencukupi")
    elif menu == 5:
        print("menu e-wallet \n 1, shopie pay \n 2. dana \n 3. gopay ")
        menu_e = int(input("silahkan pilih menu (1/2/3):"))
        if menu_e == 1:
            no_s = int (input('msaukan no shopipay anda: '))
            kredit = int(input ("jumlah yang akan di kirim: "))
            if saldo >= 5000 and kredit <= 50000000:
                saldo = saldo - kredit - admin_3
                print(f" transfer ke shopi pay berhasil \n sisa sado anda adalah {saldo}")
            else:
                print("saldo tidak mencukupi")
        elif menu_e == 2:
            no_d = int (input('msaukan no dana anda: '))
            kredit = int(input ("jumlah yang akan di kirim: "))
            if saldo >= 5000 and kredit <= 50000000:
                saldo = saldo - kredit - admin_3
                print(f" transfer ke dana   berhasil \n sisa sado anda adalah {saldo}")
            else:
                print("saldo tidak mencukupi")
        elif  menu_e == 3:
            no_g = int (input('msaukan no gopay anda: '))
            kredit = int(input ("jumlah yang akan di kirim: "))
            if saldo >= 5000 and kredit <= 50000000:
                saldo = saldo - kredit - admin_3
                print(f" transfer ke gopay berhasil \n sisa sado anda adalah {saldo}")
            else:
                print("saldo tidak mencukupi") 
    elif menu == 6:
        
        print("menu \n1. dollar \n2.yen \n3. ringgit")
        konversi = int(input ("silahkan pilih mata uang yang ingin di konversi (1/2/3)"))
       
           
                   
        