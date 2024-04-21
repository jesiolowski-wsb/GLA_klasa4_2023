wejscie=open("liczby (3).txt", "r")
wyjcie=open("wyniki.txt", "w")
dane=[]

for i in wejscie:
    dane.append(int(i.strip()))

def czy_pierwsdza(a):
    if a==1:
        return False
    if a==2:
        return True
    for i in range(2,a//2+1):
        if a%i==0:
            return False
    return True

ilosc=0
suma=0
for i in dane:
    if czy_pierwsdza(i):
        wyjcie.write(f"{i} ")
        ilosc+=1
        suma+=i

wyjcie.write("\n")

wyjcie.write(f"{ilosc=}\n")
wyjcie.write(f"{suma=}\n")


print(dane)
wyjcie.close()


wejscie.close()
