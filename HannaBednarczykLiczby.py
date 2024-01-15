with open("liczby.txt", "r") as file:
    lines = file.readlines()
data_t = []
data = []
for l in lines:
    l = l.split()
    l = list(map(int, l))
    data_t.append(l)
for a in data_t:
    data.append(a[0])

out = open("wyniki3.txt", "w")

def is_prime(x):
    if x == 1:
        return False
    if x == 2:
        return True
    else:
        for i in range(2,x):
            if x%i == 0:
                return False
    return True
prime_counter = 0
for a in data:
    if is_prime(a-1):
        prime_counter += 1

out.write(f"Zad 2\n{prime_counter}\n\n")

#Zad 3
'''
def goldbach(x):
    counter = 0
    for i in range(2,x//2 + 1):
        if is_prime(i) and is_prime(a - i):
            counter += 1
    return counter

l_min = 1000000
a_min = 0
l_max = 0
a_max = 0

for a in data:
    if l_max < goldbach(a):
        l_max = goldbach(a)
        a_max = a
    if l_min > goldbach(a):
        l_min = goldbach(a)
        a_min = a
'''
Goldbach = {}
for a in data:
    for i in range(2,a//2):
        if is_prime(i) and is_prime(a-i):
            if a in Goldbach:
                Goldbach[a] += 1
            else:
                Goldbach[a] = 1

#out.write(f"Zad 3\n{a_max} {l_max} {a_min} {l_min}")
out.write(f"Zad 3\n{max(Goldbach.items(), key=lambda x: x[1])} {min(Goldbach.items(), key=lambda x: x[1])}")#wypisuję par key:value o największym i najmniejszym value
#Zad 4
hexagon = ""
for a in data:
    hexagon += hex(a)[2::]

out.write(f"\n\nZad4\n0:{hexagon.count('0')}\n")
out.write(f"1:{hexagon.count('1')}\n")
out.write(f"2:{hexagon.count('2')}\n")
out.write(f"3:{hexagon.count('3')}\n")
out.write(f"4:{hexagon.count('4')}\n")
out.write(f"5:{hexagon.count('5')}\n")
out.write(f"6:{hexagon.count('6')}\n")
out.write(f"7:{hexagon.count('7')}\n")
out.write(f"8:{hexagon.count('8')}\n")
out.write(f"9:{hexagon.count('9')}\n")
out.write(f"A:{hexagon.count('a')}\n")
out.write(f"B:{hexagon.count('b')}\n")
out.write(f"C:{hexagon.count('c')}\n")
out.write(f"D:{hexagon.count('d')}\n")
out.write(f"E:{hexagon.count('e')}\n")
out.write(f"F:{hexagon.count('f')}\n")
