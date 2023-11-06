combined = []
data = []
retencja = []
opened = open("ekodom.txt")
for i in opened:
    combined.append(i.split())
for i in range(len(combined)):
    if i == 0:
        continue
    else:
        data.append(combined[i][0])
        retencja.append(combined[i][1])
combined.pop(0)
print(data)
print(retencja)
print(combined)
podlewany = 0
najdluzszy = 1
pocz = ""
kon = ""
current = 1
for i in range(len(retencja) - 1):
    if retencja[i] != '0':
        continue
    if current % 5 == 0:
        podlewany += 1
        print("dupa "+ str(i + 2))
    if retencja[i+1] == '0':
        current += 1
        continue
    if retencja[i+1] != '0':
        if current > najdluzszy:
            kon = data[i]
            pocz = data[i - current + 1]
            najdluzszy = current
        current = 1
print(najdluzszy)
print(pocz)
print(kon)
print(podlewany)
