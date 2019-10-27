#kalkulator cinta


def hitungKecocokan(n1,n2):
    nama1 = ""
    nama2 = ""
    jumlahNama1 = 0
    jumlahNama2 = 0
    jN1 = []
    jN2 = []
    hasilNama1 = 0
    hasilNama2 = 0

    for i in range(len(n1)):
        if ord(n1[i]) >= 65 and ord(n1[i]) <= 90:
            nama1 += chr(ord(n1[i])+32)
        else:
            nama1 += n1[i]
        
        jml = ord(nama1[i])-96
        jumlahNama1 += jml
        
    for i in range(len(n2)):
        if ord(n2[i]) >= 65 and ord(n2[i]) <= 90:
            nama2 += chr(ord(n2[i])+32)
        else:
            nama2 += n2[i]

        jml = ord(nama2[i])-96
        jumlahNama2 += jml

    for i in str(jumlahNama1):
        jN1 += i
    for i in str(jumlahNama2):
        jN2 += i

    if len(jN1) == 3:
        for i in range(len(jN1)-2):
            for j in jN1:
                hasilNama1 += int(j)
    elif len(jN1) == 2:
        for i in range(len(jN1)-1):
            for j in jN1:
                hasilNama1 += int(j)
    else:
        for i in range(len(jN1)):
            for j in jN1:
                hasilNama1 += int(j)

    if len(jN2) == 3:
        for i in range(len(jN2)-2):
            for j in jN2:
                hasilNama2 += int(j)
    elif len(jN2) == 2:
        for i in range(len(jN2)-1):
            for j in jN2:
                hasilNama2 += int(j)
    else:
        for i in range(len(jN2)):
            for j in jN2:
                hasilNama2 += int(j)

    if hasilNama1 < hasilNama2:
        cocok = hasilNama1/hasilNama2*100
    else:
        cocok = hasilNama2/hasilNama1*100
    return cocok

        
print("======= kalkulator cinta =======")
print()
n1 = input("nama pertama : ")
n2 = input("nama kedua   : ")

print("%.2f %% cocok"%hitungKecocokan(n1,n2))
