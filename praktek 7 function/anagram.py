#anagram

def cekAnagram(k1,k2):
    spasi1 = ""
    spasi2 = ""
    kalimat1 = ""
    kalimat2 = ""
    kal1 = 0
    kal2 = 0

    for i in k1:
        if i != " ":
            spasi1+=i
    for i in k2:
        if i != " ":
            spasi2+=i
    
    for i in range(len(spasi1)):
        if ord(spasi1[i]) >= 65 and ord(spasi1[i]) < 97:
            kalimat1 += chr(ord(spasi1[i])+32)
        else:
            kalimat1 += spasi1[i]

        hasil = ord(kalimat1[i])-96
        kal1+=hasil
        
    for i in range(len(spasi2)):
        if ord(spasi2[i]) >= 65 and ord(spasi2[i]) < 97:
            kalimat2 += chr(ord(spasi2[i])+32)
        else:
            kalimat2 += spasi2[i]

        hasil = ord(kalimat2[i])-96
        kal2+=hasil
        

    if kal1 != kal2:
        cek = "bukan anagram"
    else:
        cek = "anagram"
 
    return cek

print("======== anagram atau bukan anagram ? ========")
print()
input1 = input("kalimat 1 : ")
input2 = input("kalimat 2 : ")

print(cekAnagram(input1,input2))
    
