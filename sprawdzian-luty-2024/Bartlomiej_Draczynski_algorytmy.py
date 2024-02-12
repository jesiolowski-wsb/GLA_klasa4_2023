def rysuj_choinke(x):
    for i in range(1, x + 1):
        print(" " * (x - i) + "*" * (2 * i - 1))
    print(" " * (x - 1) + "|")


rysuj_choinke(2)
rysuj_choinke(8)
rysuj_choinke(100)
