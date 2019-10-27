#runtutan
'''
made by : fiqri ardiansyah
menghitung luas ,keliling dan diameter dari lingkaran.
dengan memasukan sebuah nilai dan mengeluarkan hasil luas, keliling dan diameter
dari lingkarang
'''

r = int(input("r : "))
phi = 3.14

#luas
l = phi * r * r
#keliling
k = 2 * phi * r
#diameter
d = 2 * r

print("luas : %3.f ,keliling : %1.f dan diameter : %1.f"%(l,k,d))
