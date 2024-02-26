import re
tekst = "(...) Historia przegiegu tranzakcji sklepu X: anna_kowalska@wp.pl zakupił(a) produkt od marcin.lewandowski@gmail.org jakiś czas potem sprzedając go dalej dodając marżę w wysokości 25% tak że produkt wylądował u johnDoe@sample.net. Następnie historia traci klarowność - w bazie mamy informację jedynie o adresie unknown-person@o2.pl"

x = tekst.split()
print(x)
#szuka adresow
adress = []
for a in x:
    z = re.search("[a-z0-9\.-_]+@[a-z0-9\.]+",a)#czy cos jest emailem
    if z:
        adress.append(a)
print(adress)

# szuka polskich adresow
polish_adress = []
for a in x:
    if a.endswith(".pl"):
        polish_adress.append(a)
print(f"jest {len(polish_adress)} polskich adresow a sa to: {polish_adress}")

tekst_2 = "Kontakt do naszych oddziałów: Warszawa +48 123 456 789, Berlin +49 234 567 890, Nowy Jork +1 987 654 3210, Londyn +44-843-243-3224"
y = tekst_2.split()
print(y)
'''
for a in y:
    z = re.search("\d{1,3}[\s-]?\d{1,3}[\s-]?\d{1,3}[\s-]?\d{1,4}",a) # pierwsze 1-2-3 znaki to cyfry, potem albo spacja albo - albo nic, tak jeszcze 2 razy, i ostatnie 1-2-3-4 znaki
    if z:
'''

z = re.search("\d{1,3}[\s-]?\d{1,3}[\s-]?\d{1,3}[\s-]?\d{1,4}",a) # pierwsze 1-2-3 znaki to cyfry, potem albo spacja albo - albo nic, tak jeszcze 2 razy, i ostatnie 1-2-3-4 znaki
substituted = re.sub("\d{1,3}[\s-]?\d{1,3}[\s-]?\d{1,3}[\s-]?\d{1,4}", '',"*********")
print(substituted)


def sorting(l:list):
    n = len(l)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if l[j] > l[j+1]:
                a = l[j+1]
                l[j+1] = l[j]
                l[j] = a
    return l

print(sorting([1, 3, 4, 2, 5, 2]))



import re
tekst = "(...) Historia przegiegu tranzakcji sklepu X: anna_kowalska@wp.pl zakupił(a) produkt od marcin.lewandowski@gmail.org jakiś czas potem sprzedając go dalej dodając marżę w wysokości 25% tak że produkt wylądował u johnDoe@sample.net. Następnie historia traci klarowność - w bazie mamy informację jedynie o adresie unknown-person@o2.pl"

x = tekst.split()
print(x)
#szuka adresow
adress = []
for a in x:
    z = re.search("[a-z0-9\.-_]+@[a-z0-9\.]+",a)#czy cos jest emailem
    if z:
        adress.append(a)
print(adress)

# szuka polskich adresow
polish_adress = []
for a in x:
    if a.endswith(".pl"):
        polish_adress.append(a)
print(f"jest {len(polish_adress)} polskich adresow a sa to: {polish_adress}")

tekst_2 = "Kontakt do naszych oddziałów: Warszawa +48 123 456 789, Berlin +49 234 567 890, Nowy Jork +1 987 654 3210, Londyn +44-843-243-3224"
y = tekst_2.split()
print(y)
'''
for a in y:
    z = re.search("\d{1,3}[\s-]?\d{1,3}[\s-]?\d{1,3}[\s-]?\d{1,4}",a) # pierwsze 1-2-3 znaki to cyfry, potem albo spacja albo - albo nic, tak jeszcze 2 razy, i ostatnie 1-2-3-4 znaki
    if z:
'''

z = re.search("\d{1,3}[\s-]?\d{1,3}[\s-]?\d{1,3}[\s-]?\d{1,4}",a) # pierwsze 1-2-3 znaki to cyfry, potem albo spacja albo - albo nic, tak jeszcze 2 razy, i ostatnie 1-2-3-4 znaki
substituted = re.sub("\d{1,3}[\s-]?\d{1,3}[\s-]?\d{1,3}[\s-]?\d{1,4}", '',"*********")
print(substituted)


def sorting(l:list):
    n = len(l)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if l[j] > l[j+1]:
                a = l[j+1]
                l[j+1] = l[j]
                l[j] = a
    return l

print(sorting([1, 3, 4, 2, 5, 2]))
