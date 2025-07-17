data = []
jumlah_siswa=int(input("masukan jumlah siswa yang ada: "))
for i in range (jumlah_siswa):
         print(f"\n data siswa ke {i+1}")
         nama = input("masukan nama siswa: ")
         mtk = int(input("masukan nilai: "))
         ipa = int(input("masukan nilai: "))
         ips = int(input("masukan nilai: "))
         
         data.append({
             "nama":nama,
             "mtk" :mtk,
             "ipa" :ipa,
             "ips" :ips
         })
         
print("\n ~rekap nilai siswa~")
no=1
for siswa in data:
    print(f"no {no} {siswa ["nama"] }")
    print(f"| mapel | nilai |")
    print(f"| mtk   | {siswa['mtk']}|")
    print(f"| ipa   | {siswa['ipa']}|")
    print(f"| ips   | {siswa['ips']}|\n")
    no+=1
    
    
