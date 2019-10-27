import math
print("======= latihan 15 (array) ========")
print()

angka = input("angka : ").split()

print("===== rata rata =====")
rata = 0
for i in angka:
    rata += int(i)
print("rata : ",rata/(len(angka)))



print("==== standar deviasi ====")
n = len(angka)
xi=0
x2=0

for i in angka:
    xi+=int(i)
    x2+=int(i)**2

x = xi**2
s2 = n*x2-x
s = n*(n-1)
varian = s2/s
print("%.2f "%(math.sqrt(varian)))



