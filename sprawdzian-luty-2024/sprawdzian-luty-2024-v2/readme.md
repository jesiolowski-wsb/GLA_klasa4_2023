# Wyrażenia regularne
Do rozwiązań użyj wyrażeń regularnych ([dokumentacja W3Schools](https://www.w3schools.com/python/python_regex.asp), [re docs](https://docs.python.org/3/library/re.html), [online regex tester](https://regex101.com/) [polski tutorial](https://ggoralski.gitlab.io/python-wprowadzenie/czesc_ii/2_01-regex/))

### 1: zwracanie listy wyników
Napisz program który używa wyrażeń regularnych do:
- wyszukiwania i wyświetlania wszystkich adresów e-mail zawartych w danym tekście.
- policzeniu ile ze znalezionych adresów pochodzi z serwisów w Polsce
- pokazaniu tych adresów

```
tekst = "(...) Historia przegiegu tranzakcji sklepu X: anna_kowalska@wp.pl zakupił(a) produkt od marcin.lewandowski@gmail.org jakiś czas potem sprzedając go dalej dodając marżę w wysokości 25% tak że produkt wylądował u johnDoe@sample.net. Następnie historia traci klarowność - w bazie mamy informację jedynie o adresie unknown-person@o2.pl"
```

### 2: zmiana treści wg. wzorca
Napisz program który używa funkcji `sub` z modułu re aby zanonimizować numery telefonów w podanym tekście. Program powinien zachować numery kierunkowe krajów (np. +48 dla Polski), ale zastąpić resztę numeru telefonu gwiazdkami * tak, aby ukryć rzeczywiste numery telefonów.

#### Wymagania:

Program powinien identyfikować różne formaty numerów telefonów - w tym międzynarodowe numery zaczynające się od + oraz potencjalne spacje czy myślniki w numerach
- Każdy numer telefonu powinien zostać zanonimizowany do postaci: kod kierunkowy + " *****", gdzie liczba gwiazdek odpowiada długości oryginalnego numeru bez kodu kierunkowego.
- Tekst na wejściu może zawierać różne numery telefonów z różnych krajów.

```
tekst = "Kontakt do naszych oddziałów: Warszawa +48 123 456 789, Berlin +49 234 567 890, Nowy Jork +1 987 654 3210, Londyn +44-843-243-3224"
```
powinien w wyniku działania na ekranie wyświetlić
```
Kontakt do naszych oddziałów: Warszawa +48 *********, Berlin +49 *********, Nowy Jork +1 **********, Londyn +44 **********
```


#### Podpowiedź
Frazy /  klucze do wyszukania w dokumentacji to:
- Raw String Notation
- findall, search, sub
- \d
- {}
- []
- ?
- do drugiego parametru funcji `sub` można przesłać inną funkcję

## Algorytm sortowania *********** 
Oto pseudokod jednego z algorytmów używanych do sortowania:
```
     Wejście: Tablica arr zawierająca elementy
     Wyjście: Posortowana tablica arr

 Ustal n jako długość tablicy arr
 Dla i od 0 do n-1 wykonaj:
     Dla j od 0 do n-i-2 wykonaj:
         Jeśli arr[j] > arr[j + 1] to:
             Zamień arr[j] z arr[j + 1]
 Zwróć posortowaną tablicę arr
```
> **_NOTE:_**  Zwróć uwagę na specyfikę działania range vs podany pseudokod




### Gotowe odpowiedzi wyśllij na githuba umieszczając w bieżącym folderze (tj. sprawdzian-luty-2024) w pliku / plikach ze swoim imieniem i nazwiskiem w nazwie
