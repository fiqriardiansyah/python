#latihan array

print("====== menghitung huruf vokal =======")
print()
kalimat = input("kalimat : ")
a = 0
i = 0
u = 0
e = 0
o = 0
klmt = ""
for s in range(len(kalimat)):
    if ord(kalimat[s]) >= 65 and ord(kalimat[s]) < 97:
        klmt += chr(ord(kalimat[s])+32)
    else:
        klmt += kalimat[s]
    if klmt[s] == "a":
        a+=1
    elif klmt[s] == "i":
        i+=1
    elif klmt[s] == "u":
        u+=1
    elif klmt[s] == "e":
        e+=1
    elif klmt[s] == "o":
        o+=1
 

print("vokal a = %i ,i = %i ,u = %i ,e = %i ,o = %i"%(a,i,u,e,o))
