import random

def generuj_seznam(delka):
    return [random.randint(1, 100) for _ in range(delka)]

def najdi_min_max_median(seznam):
    seznam.sort()
    delka = len(seznam)
    if delka % 2 == 0:
        median = (seznam[delka//2 - 1] + seznam[delka//2]) / 2
    else:
        median = seznam[delka//2]
    return seznam[0], seznam[-1], median

seznam = generuj_seznam(10)
print("Seznam:", seznam)
min_hodnota, max_hodnota, median = najdi_min_max_median(seznam)
print("Minimální hodnota:", min_hodnota)
print("Maximální hodnota:", max_hodnota)
print("Medianová hodnota:", median)
