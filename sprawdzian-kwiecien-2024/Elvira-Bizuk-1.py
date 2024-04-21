from collections import Counter
wejscie=open("tekst.txt","r")
dane=[]
for i in wejscie:
    dane.append(i.strip().split())
print(dane)
dl=0
for i in range(len(dane)):
    dl+=len(dane[i])
print(f"ilosc slow: {dl}")
d=[]
for i in dane:
    for j in range(len(i)):
        d.append(i[j].lower())
#print(d)
print(f"unikalne: {len(set(d))}")

dd=Counter(d)
wartosci=[]
klucze=[]
for key,value in dd.items():
    wartosci.append(value)
    klucze.append((key))
#print(wartosci)
maks=max(wartosci)
print(f"najwiecej razy: {klucze[wartosci.index(maks)]}")
wejscie.close()
