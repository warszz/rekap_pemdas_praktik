nilai = [ 90 , 80 , 75 , 85 , 88] 
print(nilai)
def cek_kelulusan (nilai):
    rata2 = sum(nilai) / len(nilai)
    if rata2 >= 70:
        print("selamat anda di nyatakan lulus")
    else:
        print("tidak lulus")
cek_kelulusan(nilai)
print ("dengan nilai rata2 anda",sum(nilai) / len(nilai))