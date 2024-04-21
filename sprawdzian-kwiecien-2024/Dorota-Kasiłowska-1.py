wejscie=open("tekst.txt", "r")
dane=[]
for i in wejscie:
    dane.append(i.strip().split())

przykad="Malu"

#ilosc slow
dicto={}
ilosc=0
tabglica=[]
for i in dane:
    for j in i:
        j=j.lower()
        if "." in j or "," in j:
            j=j[0:len(j)-1]
        if j not in dicto:
            dicto[j]=1
        else:
            dicto[j]+=1
        ilosc+=1
        tabglica.append(j)

print(len(set(tabglica)))
#odpoweidz 1
print(ilosc)


max_value=0
max_key=0
ilos_unikatowych=0
print(dicto)
for key, value in dicto.items():
    if value==1:
        ilos_unikatowych+=1
        #o te linie chodzi

    if value>max_value:
        max_value=value
        max_key=key

print(max_value)
print(max_key)
print(ilos_unikatowych)

wejscie.close()
