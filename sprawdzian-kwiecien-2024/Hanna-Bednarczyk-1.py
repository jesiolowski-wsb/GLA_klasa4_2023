with open("tekst.txt", "r") as file:
    lines = file.readlines()
data_t = []

for l in lines:
    l = l.split()
    data_t.append(l)
data_1 = []
for a in data_t:
    for i in range(len(a)):
        data_1.append(a[i])
data = []
for a in data_1:
    data.append(a.upper())
print(data)

#1
print(f"jest {len(data)} slow w tym pliku")

#2

print(f"jest {len(set(data))} unikalnych slow w tym pliku")

#3

Dict = {}

for a in data:
    if a in Dict:
        Dict[a] += 1
    else:
        Dict[a] = 1
maxkey = ""
maxval = 0
for key, value in Dict.items():
    if Dict[key] > maxval:
        maxkey = key
        maxval = value
print(f"najczesciej pojawia sie slowo {maxkey}")
