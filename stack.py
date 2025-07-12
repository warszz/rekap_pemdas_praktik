import time
import sys

def ketik_lambat(teks, delay=0.05):
    """Menampilkan teks dengan efek ketik satu per satu"""
    for karakter in teks:
        sys.stdout.write(karakter)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main_lagu():
    """Fungsi utama untuk menampilkan lirik lagu dengan timing yang pas"""
    lirik = [
        ("Sudah terbiasa terjadi tante", 0.09, 1.0),
        ("Teman datang ketika lagi butuh saja", 0.09, 1.0),
        ("Coba kalau lagi susah", 0.07, 1.3),
        ("mereka semua menghilaaang", 0.09, 0.0001),
        ("", 0.02, 0.1),  
        ("Apakah", 0.08, 0.001),
        ("Spek standar seperti ini", 0.05, 0.05),
        ("Yang para pemirsa inginkan?", 0.02, 0.00),
        ("", 0.2, 0.2), 
        ("tantee...", 0.07,0.01)
    ]
    
    for teks, ketik_delay, akhir_delay in lirik:
        ketik_lambat(teks, ketik_delay)
        time.sleep(akhir_delay)

if __name__ == "__main__":
    
    main_lagu()
    