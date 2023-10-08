# Tworzenie pustej listy ocen
oceny = []

# Dodawanie ocen za pomocą append()
oceny.append(4.5)
oceny.append(5.0)
oceny.append(2.0)
oceny.append(4.0)
oceny.append(4.5)

# Wyświetlanie listy ocen
print("Lista ocen ucznia:")
print(oceny)

# Wstawianie oceny na określonym miejscu za pomocą insert()
# (poprawka oceny)
oceny.insert(2, 4.0)

# Wyświetlanie listy ocen
print("Lista ocen ucznia po zmianie oceny:")
print(oceny)

# Usuwanie oceny z określonego indeksu za pomocą pop()
# pomylka nauczyciela - ocena miala sie poprawic - trzeba usunac
usunieta_ocena = oceny.pop(3)
print(f"Usunięta ocena: {usunieta_ocena}")
print("Lista ocen po usunięciu zbytecznej oceny:")
print(oceny)

# Usuwanie konkretnej oceny za pomocą remove()
# nauczyciel nieogar - jedna z 4.0 to nie tego ucznia - trzeba usunac
usunieta_ocena_2 = 4.0
oceny.remove(usunieta_ocena_2)
print(f"Lista ocen po usunięciu {usunieta_ocena_2} innego ucznia:")
print(oceny)

# Usuwanie elementu z określonego indeksu za pomocą del
# oceny semestralne
del oceny[1:]
print("Lista ocen po usunięciu drugiego i trzeciego elementu:")
print(oceny)

# Czyszczenie całej listy ocen za pomocą clear()
oceny.clear()
print("Lista ocen po wyczyszczeniu:")
print(oceny)
