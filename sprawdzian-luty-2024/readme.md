# Sprawdzian ze znajomości języka python 12.02.2024

> Uwaga: **Bonusowe** punkty za kreatywnośc w rozwiązywaniu (dodanie kolorków, ascii-art, obsługi błędów, eksportu do pliku, dodatkowych funkcjonalności, elementów animacji - cokolwiek wpadnie wam do głowy :) )

### SEKCJA A: Algorytmy
1. stwórz funkcjonalność *rysuj_choinkę* która dla wywołania *rysuj_choinkę(2)* na ekranie wydrukuje
```
 *
***
 |
```
dla parametru 8 zaś, 
```
       *
      ***
     *****
    *******
   *********
  ***********
 *************
***************
       |
```
ergo: 1 parametr na wejscie (i w zaleznosci od niego tyle poziomów choinki). Dodatkowo 'pień' choinki na 1 znak

### SEKCJA B: Wyrażenia regularne
W pliku `numery.txt` zapisanych jest 1000 numerów telefonów (jeden numer na wiersz). Numery telefonów są zapisane bez żadnych dodatkowych znaków (tylko cyfry). Maksymalna długość numeru telefonicznego to 15 cyfr. Przykładowe numery w tym pliku to:

8532920888
6105000455181
646454074

Zadania do wykonania:
1. Podaj liczbę numerów telefonów, które zawierają co najmniej trzy te same cyfry obok siebie (np. 111, 222 itd.).
2. Wszystkie numery telefonów o tej samej liczbie cyfr tworzą jedną "rodzinę". Podaj liczbę niepustych rodzin numerów telefonów.
3. Każdą rodzinę numerów telefonów zapisz w oddzielnym wierszu pliku `rodziny_numerow.txt`. Numery każdej rodziny wymień w kolejności rosnącej, oddzielone jedną spacją.

### SEKCJA C: OOP (object-oriented-programming)
1. Stwórz klasę **BankAccount** odpowiedzialną za konto bankowe z metodami dostępowymi:
- deposit
- withdraw
- get_balance

upewnij się że przy próbie dostępu do instancji jako stringa, na ekranie zostanie wyświetlony stan konta oraz informacja o właściecielu (np. Wlasciciel konta: [wlasciciel_konta], stan konta: [suma_zasobów])


2. Stwórz klasę **Bank** odpowiedzialną za powiązanie kont bankowych z bankiem z metodami dostępowymi:
- add_account
- get_total_balance

upewnij się że przy próbie dostępu do instancji jako stringa, na ekranie zostanie wyświetlona informacja o Banku (np. Bank [X], liczba kont: [Y])


3. Uruchom aplikację dostarczając dane do klasy Bank (tj. [nazwa_banku]) i podepnij do niego dwa konta


4. dodaj funkcjonalność historii operacji na koncie bankowym
   

5. dodaj funkcjonalnosc **menu** gdzie operator bedzie miec mozliwosc uzywania dostepnych metod 


### Gotowe odpowiedzi wyśllij na githuba umieszczając w bieżącym folderze (tj. sprawdzian-luty-2024) w pliku ze swoim imieniem i nazwiskiem w nazwie



