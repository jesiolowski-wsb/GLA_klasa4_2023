import re

tekst="Historia przegiegu tranzakcji sklepu X: anna_kowalska@wp.pl zakupił(a) produkt od marcin.lewandowski@gmail.org jakiś czas potem sprzedając go dalej dodając marżę w wysokości 25% tak że produkt wylądował u johnDoe@sample.net. Następnie historia traci klarowność - w bazie mamy informację jedynie o adresie unknown-person@o2.pl"
txt="anna_kowalska@wp.pl"


x = re.findall("[a-z\._]+@+[a-z0-9\.]+[a-z]", tekst)
print(x)

licznik=0
for i in x:
    if i.endswith("pl"):
        licznik+=1
        print(i)
print(licznik)

'''Wejście: Tablica arr zawierająca elementy
     Wyjście: Posortowana tablica arr

 Ustal n jako długość tablicy arr
 Dla i od 0 do n-1 wykonaj:
     Dla j od 0 do n-i-2 wykonaj:
         Jeśli arr[j] > arr[j + 1] to:
             Zamień arr[j] z arr[j + 1]
 Zwróć posortowaną tablicę arr'''

lista=[1, 3, 4, 2, 5, 2]
def sortowanie(n):
    for i in range(len(n)):
        for j in range(len(n)-1):
            if n[j]>n[j+1]:
                n[j], n[j+1]= n[j+1],n[j]

    return n

print(sortowanie(lista))


t = "Kontakt do naszych oddziałów: Warszawa +48 123 456 789, Berlin +49 234 567 890, Nowy Jork +1 987 654 3210, Londyn +44-843-243-3224"
t1="+48 123 456 789"
y = re.findall("[\+]+\d{1,3}[\s-]?\d{3}[\s-][\s-]?\d{3}[\s-]?\d{3,4}", t)
print(y)
