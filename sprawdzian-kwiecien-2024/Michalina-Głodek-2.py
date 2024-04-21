liczby_pierwsze = []

def pierwsza(liczba):
    if liczba <=1:
        return False
    for i in range(2, int(liczba**0.5)+1):
        if liczba % i ==0:
            return False
    return True

with open ("liczby.txt" , "r") as file:
    for line in file:
        liczba = int(line.strip())
        if pierwsza(liczba):
            liczby_pierwsze.append(liczba)

wynik = "wyniki.txt"

with open("wyniki.txt" , "w") as file:
    for pierwsze in liczby_pierwsze:
        file.write(str(pierwsze)+ "\n")

    suma = sum(liczby_pierwsze)

print(f"liczby pierwsze: {liczby_pierwsze}")
print(f"suma liczb pierwszych: {suma}")
