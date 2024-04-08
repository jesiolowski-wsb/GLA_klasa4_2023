def czyPrime(n):
    n = int(n)
    if n == 2:
        return True
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    else:
        return True


with open("tekst.txt", "r") as f:
    liczby = f.readlines()

pierwsze = []

for liczba in liczby:
    liczba = int(liczba.strip())
    if czyPrime(liczba):
        pierwsze.append(liczba)

print(f"Liczby pierwsze: {pierwsze}")
print(f"Ich suma: {sum(pierwsze)}")

with open("wyniki.txt", "w") as g:
    g.write(f"Liczby pierwsze: {pierwsze}\n")
    g.write(f"Ich suma: {sum(pierwsze)}")
