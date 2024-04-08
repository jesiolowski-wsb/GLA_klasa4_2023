import collections
import string

with open("tekst.txt") as f:
    tekst = f.read()
    print(tekst)
    tekst = tekst.translate(str.maketrans("", "", string.punctuation)).lower()
    slowa = tekst.split()
    print(slowa)

b = collections.Counter(slowa)

print(f"Slow jest: {len(slowa)}")
print(f"Slow różnych jest: {len(set(slowa))}")
print(f"Najczesciej wystepuje: {b.most_common()[0][0]}")

