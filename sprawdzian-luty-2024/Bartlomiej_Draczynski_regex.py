import re


def count_phone_numbers(h):
    with open(h, 'r') as file:
        data = file.read()
        pattern = re.compile(r'(\d)\1{2,}')
        matches = pattern.findall(data)
        return len(matches)


def count_phone_number_families(h):
    with open(h, 'r') as file:
        data = file.read().splitlines()
        families = set()
        for line in data:
            numbers = line.split()
            for number in numbers:
                families.add(len(number))
        return len(families)


x = 'numbers.txt'
print(count_phone_numbers(x))
print(count_phone_number_families(x))
