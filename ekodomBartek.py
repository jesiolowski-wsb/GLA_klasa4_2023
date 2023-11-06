plik = open("ekodom.txt", "r")
dane = []
plik.readline()
for wiersz in plik:
    wiersz = wiersz.strip()
    data, retencja = wiersz.split()
    retencja = int(retencja)
    dane.append((data, retencja))
plik.close()
ao = 0 #aktualny okres
no = 0 #najdluzszy okres
pocz = ""
kon = ""
for data, retencja in dane:
    if retencja == 0:
        ao += 1
        if ao > no:
            no = ao
            kon = data
            pocz = dane[len(dane) - ao][0]
    else:
        ao = 0
print(f"Najdłuższy okres bez opadów trwał {no} dni.")
print(f"Data początku: {pocz}")
print(f"Data końca: {kon}")
