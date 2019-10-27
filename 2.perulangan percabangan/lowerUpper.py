#merubah huruf gaya penulisan huruf

'''

made by : fiqri ardiansyah

masukan = masukan sembarang kalimat yang memiliki uppercase dan lowercase
maka kalimat akan dirubah ke lowercase dan uppercase
'''

print("===== merubah penulisan huruf =====")

kalimat = input("kalimat : ")
lower = ""
upper = ""

for i in range(len(kalimat)):
    if ord(kalimat[i]) >= 65 and ord(kalimat[i]) <= 90:
        lower += chr(ord(kalimat[i])+32)
    else:
        lower += kalimat[i]
    if ord(kalimat[i]) >= 97 and ord(kalimat[i]) <= 122:
        upper += chr(ord(kalimat[i])-32)
    else:
        upper += kalimat[i]
    
     
print("lower = ",lower)
print("upper = ",upper)

