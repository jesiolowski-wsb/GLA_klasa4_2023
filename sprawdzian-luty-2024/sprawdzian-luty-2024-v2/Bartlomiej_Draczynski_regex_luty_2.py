import re

tekst = "Kontakt do naszych oddziałów: Warszawa +48 123 456 789, Berlin +49 234 567 890, Nowy Jork +1 987 654 3210, Londyn +44-843-243-3224"

nr = r"\+\d[\d\s-]+"

def anon(n):
  return re.sub(nr, lambda m: m[0][0:3] + "*" * (len(m[0]) - 3), n)

print(tekst)
print(anon(tekst))
