#latihan array

print("===== menghitung ganjil genap ======")
print()
arr = input("kumpulan angka : ").split()

jumlah_gjl = 0
jumlah_gnp = 0
total_gjl = 0
total_gnp = 0
for i in arr:
    if int(i) % 2 == 0:
        jumlah_gnp+= 1
        total_gnp+= int(i)
    else:
        jumlah_gjl+= 1
        total_gjl+= int(i)

print("jumlah angka ganjil = %i buah "%jumlah_gjl)
print("jumlah angka genap = %i buah"%jumlah_gnp)
print("total angka ganjil = %i "%total_gjl)
print("total angka genap = %i "%total_gnp)

