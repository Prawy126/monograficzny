import matplotlib.pyplot as plt

# Definicja przedziałowych zbiorów rozmytych
# Każdy zbiór zawiera listę przedziałów [dolna granica, górna granica]
A = [[0.0, 1.0], [0.5, 1.0], [0.6, 0.8], [0.4, 0.7], [0.0, 1.0], [0.0, 1.0]]
B = [[0.4, 0.7], [0.0, 1.0], [0.6, 0.9], [0.4, 0.8], [1.0, 1.0], [1.0, 1.0]]
C = [[1.0, 1.0], [0.0, 1.0], [0.9, 0.9], [0.0, 1.0], [1.0, 1.0], [1.0, 1.0]]
D = [[0.4, 0.7], [0.2, 1.0], [0.2, 1.0], [0.4, 0.8], [0.5, 1.0], [0.5, 0.8]]
E = [[0.5, 0.6], [0.5, 1.0], [0.6, 0.8], [0.5, 0.9], [0.8, 1.0], [0.8, 1.0]]

# Negacja przedziału
# Funkcja zwraca przedział będący negacją przekazanego przedziału
def negacja(przedzial):
    return [round(1 - przedzial[1], 4), round(1 - przedzial[0], 4)]

# Agregacja
# Funkcja zwraca średnią arytmetyczną dwóch przedziałów
def agregacja(x, y):
    return [round((x[0] + y[0]) / 2, 4), round((x[1] + y[1]) / 2, 4)]

# Częściowy porządek
# Sprawdza, czy jeden przedział jest w pełni mniejszy niż drugi
def porzadek_czesciowy(x, y):
    if x[0] < y[0] and x[1] < y[1]:
        return True
    return False

# Możliwy porządek
# Sprawdza, czy przedziały nachodzą na siebie
def possible_order(x, y):
    return x[0] < y[1] and y[0] < x[1]

# Szerokość przedziału
# Oblicza szerokość przedziału
def width(interval):
    return interval[1] - interval[0]

# Miara pierwszeństwa
# Oblicza miarę pierwszeństwa jednego przedziału nad drugim
def precedence(x, y):
    if x == y:
        return [1 - (x[1] - x[0]), 1]
    elif porzadek_czesciowy(x, y):
        return [1, 1]
    else:
        l = (1 - x[1] + y[0]) / 2
        u = (1 - x[0] + y[1]) / 2
        return [l, u]

# Miara podobieństwa
# Oblicza miarę podobieństwa między przedziałami dwóch zbiorów
def similarity(A, AN):
    s_values = []
    for a, an in zip(A, AN):
        prec_1 = precedence(a, an)
        prec_2 = precedence(an, a)
        s = min(prec_1[0], prec_2[0]), min(prec_1[1], prec_2[1])
        s_values.append(s)
    return s_values

# Średnia przedziałów
# Oblicza średnią arytmetyczną dwóch przedziałów
def mean_interval(interval1, interval2):
    return [(interval1[0] + interval2[0]) / 2, (interval1[1] + interval2[1]) / 2]

# Procesowanie przedziałów
# Rekursywnie łączy przedziały w jeden, obliczając ich średnie
def process_intervals(intervals):
    while len(intervals) > 1:
        result = []
        length = len(intervals)
        for i in range(0, length - 1, 2):
            result.append(mean_interval(intervals[i], intervals[i + 1]))
        if length % 2 != 0:
            result.append(intervals[-1])
        intervals = result
    return intervals[0]

# Główna część programu
# Obliczanie negacji dla każdego zbioru
AN = [negacja(interval) for interval in A]
BN = [negacja(interval) for interval in B]
CN = [negacja(interval) for interval in C]
DN = [negacja(interval) for interval in D]
EN = [negacja(interval) for interval in E]

results = []

# Wyświetlanie wyników dla zbioru A
print("Wynik dla zbioru A")
result_A = process_intervals(similarity(A, AN))
results.append(('A', result_A))
print(result_A)

# Wyświetlanie wyników dla zbioru B
print("\n\nWynik dla zbioru B")
result_B = process_intervals(similarity(B, BN))
results.append(('B', result_B))
print(result_B)

# Wyświetlanie wyników dla zbioru C
print("\n\nWynik dla zbioru C")
result_C = process_intervals(similarity(C, CN))
results.append(('C', result_C))
print(result_C)

# Wyświetlanie wyników dla zbioru D
print("\n\nWynik dla zbioru D")
result_D = process_intervals(similarity(D, DN))
results.append(('D', result_D))
print(result_D)

# Wyświetlanie wyników dla zbioru E
print("\n\nWynik dla zbioru E")
result_E = process_intervals(similarity(E, EN))
results.append(('E', result_E))
print(result_E)

print()
print("-------------------------------------------------------------")
print("Posortowane entropie według porządku possible:")

# Sortowanie wyników
# Funkcja sortuje listę wyników zgodnie z możliwym porządkiem
def custom_sort(intervals):
    n = len(intervals)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Sprawdzamy, czy możliwe w obie strony
            if possible_order(intervals[j][1], intervals[j + 1][1]) and possible_order(intervals[j + 1][1], intervals[j][1]):
                # Jeśli możliwe w obie strony, sortujemy według szerokości
                if width(intervals[j][1]) > width(intervals[j + 1][1]):
                    intervals[j], intervals[j + 1] = intervals[j + 1], intervals[j]
            elif possible_order(intervals[j][1], intervals[j + 1][1]):
                intervals[j], intervals[j + 1] = intervals[j + 1], intervals[j]
    # Zaokrąglamy wyniki do czterech miejsc po przecinku
    for i in range(len(intervals)):
        intervals[i] = (intervals[i][0], [round(intervals[i][1][0], 4), round(intervals[i][1][1], 4)])
    return intervals

sorted_results = custom_sort(results)
print(sorted_results)

# Tworzenie wykresu
zbior_names = [r[0] for r in sorted_results]
interval_values = [r[1] for r in sorted_results]

plt.figure(figsize=(10, 6))
for i, (zbior, interval) in enumerate(zip(zbior_names, interval_values)):
    plt.plot(interval, [i, i], marker='o', label=f'{zbior}: {interval}')

plt.yticks(range(len(zbior_names)), zbior_names)
plt.xlabel('Wartości przedziałów')
plt.ylabel('Zbiory')
plt.title('Wizualizacja przedziałów zbiorów')
plt.legend()
plt.show()
