with open("sygnaly.txt", "r") as f:
    sygnaly = [i.strip() for i in f]

sygnalyile = [set(list(i)) for i in sygnaly]
sygnalyile1 = [len(i) for i in sygnalyile]

text = []

for sygnal in sygnaly:
    if (sygnaly.index(sygnal) + 1) % 40 == 0:
        text.append(sygnal[9])

a = ''.join(text)

print(a)
print(sygnaly[sygnalyile1.index(max(sygnalyile1))], max(sygnalyile1))
for sygnal in sygnaly:
    if int(ord(max(sygnal))) - int(ord(min(sygnal))) <= 10:
        print(sygnal)
