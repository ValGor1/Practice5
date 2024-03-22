N = int(input())
Sic = N // 29
Gal = Sic // 17
Knat = N % 29
Sic_ost = Sic - 17
print(Gal,'галлеонов')
print(Sic_ost,'сикелей')
print(Knat,'кнатов')