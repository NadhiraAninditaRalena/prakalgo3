print("@@@ @  @@@ @@@@   @   @ @ @@@@@@     @@@")
print("@ @ @ @  @ @   @  @   @ @ @     @   @   @")
print("@ @ @ @@@@ @  @   @@@@@ @ @@@@@@    @@@@@")
print("@ @@@ @  @ @@     @   @ @ @    @    @   @")

# Input angka awal dan akhir
angka_awal = int(input("Masukkan angka awal: "))
angka_akhir = int(input("Masukkan angka akhir: "))

# Periksa apakah angka_awal lebih kecil dari angka_akhir
if angka_awal > angka_akhir:
    angka_awal, angka_akhir = angka_akhir, angka_awal

# tampilkan angka dengan urutan yang dimodifikasi menggunakan while
i = angka_awal
j = angka_akhir

while i < j:
    print(i,j)
    i += 1
    j -= 1
    
    
    
    
    


