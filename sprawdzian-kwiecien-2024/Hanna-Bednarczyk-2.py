with open("liczby.txt", "r") as file:
    lines = file.readlines()
data = []
for l in lines:
    l = l.split()
    data.append(int(l[0]))

print(data)

out = open("wyniki.txt", "w")

def prime(x):
    if x < 2:
        return False
    else:
        for i in range(2,int(x**0.5) + 1):
            if x % i == 0:
                return False
        return True

prime_sum = 0
prime_list = []
for x in data:
    if prime(x):
        prime_sum += x
        prime_list.append(x)
print(len(prime_list))
out.write(f"liczby pierwsze to: {prime_list}, a ich suma to {prime_sum}")
