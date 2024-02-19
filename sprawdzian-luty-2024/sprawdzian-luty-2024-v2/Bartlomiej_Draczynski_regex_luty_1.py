import re

tekst = "(...) Historia przegiegu tranzakcji sklepu X: anna_kowalska@wp.pl zakupił(a) produkt od marcin.lewandowski@gmail.org jakiś czas potem sprzedając go dalej dodając marżę w wysokości 25% tak że produkt wylądował u johnDoe@sample.net. Następnie historia traci klarowność - w bazie mamy informację jedynie o adresie unknown-person@o2.pl"

pattern = r"\w+@\w+\.\w+"
adresy = re.findall(pattern, tekst)
print("Znalezione maile: ")
for adres in adresy:
    print(adres)

pl = 0
for adres in adresy:
    if adres.endswith(".pl"):
        pl += 1

print(f"Polskich adresów jest: {pl}")

print("I są to: ")
for adres in adresy:
    if adres.endswith(".pl"):
        print(adres)
