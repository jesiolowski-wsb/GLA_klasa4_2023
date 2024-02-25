tekst = "(...) Historia przegiegu tranzakcji sklepu X: anna_kowalska@wp.pl zakupił(a) produkt od marcin.lewandowski@gmail.org jakiś czas potem sprzedając go dalej dodając marżę w wysokości 25% tak że produkt wylądował u johnDoe@sample.net. Następnie historia traci klarowność - w bazie mamy informację jedynie o adresie unknown-person@o2.pl"

# Napisz program który używa wyrażeń regularnych do:
#
# wyszukiwania i wyświetlania wszystkich adresów e-mail zawartych w danym tekście.
# policzeniu ile ze znalezionych adresów pochodzi z serwisów w Polsce
# pokazaniu tych adresów

#zad 1

import re


x=re.findall("[a-z\._]+@[a-z0-9\.]+", tekst)

licznik=0
for i in x:
    if i.endswith("pl"):
        licznik+=1
        print(i)

print(licznik)

#Napisz implementację algorytmu przedstawionego w pseudokodzie i przekaż do funkcji [1, 3, 4, 2, 5, 2] Jako wynik funkcji oczekujemy listy [1, 2, 2, 3, 4, 5]


 # Ustal n jako długość tablicy arr
 # Dla i od 0 do n-1 wykonaj:
 #     Dla j od 0 do n-i-2 wykonaj:
 #         Jeśli arr[j] > arr[j + 1] to:
 #             Zamień arr[j] z arr[j + 1]
 # Zwróć posortowaną tablicę arr

tab=[1, 3, 4, 2, 5, 2]


def sortowanie_bambelkowe(a):
    posortowane=sorted(a)
    n=len(a)
    for i in range(n):
        for j in range(n-1):
            if posortowane[j]>posortowane[j+1]:
                posortowane[j], posortowane[j+1]=posortowane[j+1], posortowane[j]
    return posortowane

print(sortowanie_bambelkowe(tab))

txt="Kontakt do naszych oddziałów: Warszawa +48 123 456 789, Berlin +49 234 567 890, Nowy Jork +1 987 654 3210, Londyn +44-843-243-3224"
txt.split()
y=re.findall("[0-9\+ -]+", txt)

print(y)
[\s-]?\d{3}[\s-]?\d{3}[\s-]?\d{3,4}
