---
layout: default
---

# PROJEKT GRUPA 5

### - Kod programu:

```python


# Definicja przedziałowych zbiorów rozmytych
A = [[0.0, 1.0], [0.5, 1.0], [0.6, 0.8], [0.4, 0.7], [0.0, 1.0], [0.0, 1.0]]
B = [[0.4, 0.7], [0.0, 1.0], [0.6, 0.9], [0.4, 0.8], [1.0, 1.0], [1.0, 1.0]]
C = [[1.0, 1.0], [0.0, 1.0], [0.9, 0.9], [0.0, 1.0], [1.0, 1.0], [1.0, 1.0]]
D = [[0.4, 0.7], [0.2, 1.0], [0.2, 1.0], [0.4, 0.8], [0.5, 1.0], [0.5, 0.8]]
E = [[0.5, 0.6], [0.5, 1.0], [0.6, 0.8], [0.5, 0.9], [0.8, 1.0], [0.8, 1.0]]

# Negacja przedziału
def negacja(przedzial):
    return [round(1 - przedzial[1], 4), round(1 - przedzial[0], 4)]

# Agregacja
def agregacja(x, y):
    return [round((x[0] + y[0]) / 2, 4), round((x[1] + y[1]) / 2, 4)]

def porzadek_czesciowy(x, y):
    if x[0] <= y[0] and x[1] <= y[1]:
        return True
    return False

# Miara pierwszeństwa
def pierwszenstwo(x, y):
    if x == y:
        return [round(1 - (x[1] - x[0]), 4), 1]
    elif porzadek_czesciowy(x, y):
        return [1, 1]
    else:
        l = round((1 - x[1] + y[0]) / 2, 4)
        u = round((1 - x[0] + y[1]) / 2, 4)
        return [l, u]

# Miara podobieństwa
def podobienstwo(A, AN):
    wartosci_podobienstwa = []
    for a, an in zip(A, AN):
        pierwsz_1 = pierwszenstwo(a, an)
        pierwsz_2 = pierwszenstwo(an, a)
        s = min(pierwsz_1[0], pierwsz_2[0]), min(pierwsz_1[1], pierwsz_2[1])
        wartosci_podobienstwa.append(s)
    return wartosci_podobienstwa

# Średnia z dwóch przedziałów
def srednia_przedzialow(przedzial1, przedzial2):
    """
    Oblicza średnią dwóch przedziałów.
    """
    return [round((przedzial1[0] + przedzial2[0]) / 2, 4), round((przedzial1[1] + przedzial2[1]) / 2, 4)]

# Przetwarzanie listy przedziałów
def przetwarzanie_przedzialow(przedzialy, nazwa):
    """
    Przetwarza listę przedziałów za pomocą funkcji srednia_przedzialow, aż pozostanie tylko jeden przedział.
    Wyświetla nazwę zbioru i numer iteracji dla każdej iteracji.
    """
    print(f"Zbiór {nazwa}:")
    print("   Iteracja 0:", ", ".join(map(str, przedzialy)))  # Wyświetlenie początkowego zestawu przedziałów
    iteracja = 1
    while len(przedzialy) > 1:
        wynik = []
        dlugosc = len(przedzialy)

        # Iteracja przez przedziały parami
        for i in range(0, dlugosc - 1, 2):
            wynik.append(srednia_przedzialow(przedzialy[i], przedzialy[i + 1]))

        # Jeśli liczba przedziałów jest nieparzysta, przenieś ostatni nieparzysty przedział do następnej rundy
        if dlugosc % 2 != 0:
            wynik.append(przedzialy[-1])

        przedzialy = wynik

        # Drukowanie nazwy zbioru i numeru iteracji z wcięciem
        wciecie = " " * (6 * (iteracja - 1)) + " " * (3 * (iteracja - 1))
        print(" " * 15, wciecie, "Iteracja", iteracja, ":", ", ".join(map(str, przedzialy)))

        iteracja += 1

    return przedzialy[0]

# Obliczenie negacji dla każdego zbioru
AN = [negacja(przedzial) for przedzial in A]
BN = [negacja(przedzial) for przedzial in B]
CN = [negacja(przedzial) for przedzial in C]
DN = [negacja(przedzial) for przedzial in D]
EN = [negacja(przedzial) for przedzial in E]

wyniki = []

# Przetwarzanie i wyświetlanie wyników dla każdego zbioru
print("Wyniki dla zbiorów:")
wynik_A = przetwarzanie_przedzialow(podobienstwo(A, AN), 'A')
wyniki.append(('A', wynik_A))

wynik_B = przetwarzanie_przedzialow(podobienstwo(B, BN), 'B')
wyniki.append(('B', wynik_B))

wynik_C = przetwarzanie_przedzialow(podobienstwo(C, CN), 'C')
wyniki.append(('C', wynik_C))

wynik_D = przetwarzanie_przedzialow(podobienstwo(D, DN), 'D')
wyniki.append(('D', wynik_D))

wynik_E = przetwarzanie_przedzialow(podobienstwo(E, EN), 'E')
wyniki.append(('E', wynik_E))

# Sortowanie wyników według warunku x ≤ y
posortowane_wyniki = sorted(wyniki, key=lambda x: x[1][0])

print("\nWyniki po sortowaniu possible:")

for nazwa, przedzial in posortowane_wyniki:
    print(f"Zbiór {nazwa}: {przedzial}")



```
