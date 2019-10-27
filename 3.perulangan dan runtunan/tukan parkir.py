#program tukang parkir

'''

made by : fiqri ardiansyah


program ini akan menjumlah pendapatan tukan parkir berdasarkan jumlah mobil
dan motor yang terparkir, mobil akan bernili 5000 dan motor akan bernilai 2000
pendapatan tukang parkir akan dijumlah dari mobil dan motor yang terparkir
'''

print("==== uang tukang parkir =====")
print()
mobil = int(input("masukkan jumlah mobil yang terparkir : "))
motor = int(input("masukkan jumlah motor yang terparkir : "))

mbl = 5000
mtr = 2000

uang = 0
for i in range(mobil):
    uang+=mbl
for i in range(motor):
    uang+=mtr

print("uang tukang parkir saat ini : Rp.",uang)
