kalimat = " UNIVERSITAS NUSA PUTRA SUKABUMI "

#MENGAMBIL KATA (PUTRA NUSA)
kata_pertama = kalimat.split()[2] + " " + kalimat.split()[1]
print(kata_pertama)

#MENGAMBIL KATA (NIVERSITAS NSA PTRA SKABMI)
kata_kedua = kalimat[1:11] + " " + kalimat[14:18] + " " + kalimat[18] + " " + kalimat[20:24] + " " + kalimat[25:]
print(kata_kedua)

#MENGAMBIL KATA (SUKABUMI PUTRA NUSA UNIVERSITAS)
kata_ketiga = kalimat.split()[::-1] 
print(kata_ketiga)

#MENGAMBIL KATA (UNPS)
kata_keempat = kalimat.split()[0][0] + " " + kalimat.split()[1][0] + " " + kalimat.split()[2][0] + " " + kalimat.split()[3][0]
print(kata_keempat)

#MENGAMBIL KATA (TAS SAPU BUMI )
kata_kelima = kalimat.split()[0][-3:] + " " + kalimat.split()[2] + " " + kalimat.split()[-1]
print(kata_kelima)
