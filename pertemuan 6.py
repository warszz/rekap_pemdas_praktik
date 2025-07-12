# for a in range (1,11) :
#     print("angka saat ini ",a)
    
#latiahan 
# for a in range (1,11) :
#     if a % 3 == 0 :
#         print(f"{a},yes")
#         continue
#     print (a)


#latihan
nama = ['yaya','lilis','dadang','fitri']
cari = input("nama yang di cari: ")

if cari in nama:
    urutan = (nama.index(cari))+1
    print(f"nama ada dengan urutan ke-{urutan}")