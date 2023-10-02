# https://arkusze.pl/maturalne/informatyka-2023-czerwiec-matura-rozszerzona.pdf
def iloczyn(x, y):
    if y == 1:
        return x
    else:
        k = y // 2
        z = iloczyn(x, k)
        if y % 2 == 0:
            return z + z
        else:
            return x + z + z

# Przykładowe użycie:
x = 9
y = 11
wynik = iloczyn(x, y)
print(f"Iloczyn {x} * {y} = {wynik}")
