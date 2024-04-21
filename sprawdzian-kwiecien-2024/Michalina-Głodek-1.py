from collections import Counter
with open ("tekst.txt", "r") as file:
    tekst = file.read().lower()
    tekst = tekst.split()
    
print(f"ilosc slow:{len(tekst)}")

wynik = set(tekst)
print(f"ilosc unikalnych slow:{len(wynik)}")

licznik = Counter(tekst)
ilosc = []
slowo = []
for key, value in licznik.items():
    ilosc.append(value)
    slowo.append(key)
max_wystep = max(ilosc)
print(f"najczesciej wystepujace slowo: {slowo[ilosc.index(max_wystep)]}")
