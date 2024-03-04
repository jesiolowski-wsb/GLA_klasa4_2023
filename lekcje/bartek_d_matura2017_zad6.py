def palindrom(m):
    return m == m[::-1]


ile = 0

with open("dane.txt", "r") as f:
    dane = [list(map(int,wiersz.split())) for wiersz in f]


pixele = [piksel for wiersz in dane for piksel in wiersz]
max = max(pixele)
min = min(pixele)

for wiersz in dane:
    if not palindrom(wiersz):
        ile += 1

ile1 = 0
for i in range(0, 200):
    for j in range(0, 320):
        if j < 319 and abs(dane[i][j] - dane[i][j + 1]) > 128:
            ile1 += 1
        if i < 199 and abs(dane[i][j] - dane[i + 1][j]) > 128:
            ile1 += 1

print(f"Najjasniejszy ma: {max}")
print(f"Najciemniejszy ma: {min}")
print(ile)
print(ile1)


with open("wyniki6.txt","w") as g:
    g.write(f"Najjasniejszy ma: {max}")
    g.write(f"Najciemniejszy ma: {min}")

