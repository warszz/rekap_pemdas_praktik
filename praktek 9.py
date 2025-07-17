data_siswa={
    "nama" : [],
    "nilai ilal": [88,70,90],
    "mata plajaran ilal":["mtk","ipa","ips"],
    "nilai agoy": [77, 78, 80],
    "mata plajaran agoy":["mtk","ipa","ips"],
}
data_siswa["nama"].extend(["ilal","agoy"])
print(f"nilai {data_siswa["nama"][0]}:", data_siswa["mata plajaran ilal"],data_siswa["nilai ilal"])
print(f"nilai {data_siswa["nama"][-1]}:", data_siswa["mata plajaran agoy"],data_siswa["nilai agoy"])