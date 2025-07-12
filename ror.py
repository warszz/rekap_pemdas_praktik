nilai = [ 90 , 80 , 75 , 85 , 88] 

def cek_kelulusan (nilai):
    rata2 = sum(nilai) / len(nilai)
    if rata2 >= 70:
        print("lulus")
    else:
        print("tidak lulus")
        
