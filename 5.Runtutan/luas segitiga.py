#runtutan
'''

made by : fiqri ardiansyah


rumus mencari keliling dan luas segitiga sama kaki
masukan : untuk mencari keliling = sisi
            untuk mencari luas = alas dan tinggi
keluarang : hasil keliling dan luas

'''

print("==== mencari keliling segitiga sama kaki====")
sisi1 = int(input("sisi 1 : "))
sisi2 = int(input("sisi 2 : "))
sisi3 = int(input("sisi 3 : "))

keliling = sisi1 + sisi2 + sisi3
print("keliling : ",keliling)
print()
print("==== mencari luas segitiga sama kaki =====")
alas = int(input("alas : "))
tinggi = int(input("tinggi : "))

luas = 0.5 * alas * tinggi
print("luas : ",luas)
