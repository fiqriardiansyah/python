#runtutan
'''

made by : fiqri ardiansyah


konversi detik ke jam dan menit
memasukan detik(integer) dan mengubah nya menjadi jam dan menit
'''

det = int(input("detik : "))

jam = det//3600
me = det%3600
menit = me /3600
print(menit)
print("%.1f jam %.2f menit"%(jam,menit))
