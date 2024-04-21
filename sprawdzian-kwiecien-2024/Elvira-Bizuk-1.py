import math
wejscie=open("liczby.txt","r")
dane=[]
for i in wejscie:
    dane.append(int(i.strip()))
print(dane)

def czy_pierwsza(n):
    if n==1:
        return False
    for i in range(2, int(math.sqrt(n))+1):
        if n%i==0:
            return False
    return True

pierwsze=[]
for i in dane:
    if czy_pierwsza(i):
        pierwsze.append(i)
print(f"ile pierwszych:{len(pierwsze)}")
suma=0

for i in pierwsze:
    suma+=i
print(f"suma:{suma}")
