import numpy as np

# Definicja przedziałowych zbiorów rozmytych
A = [[0.0, 1.0], [0.5, 1.0], [0.6, 0.8], [0.4, 0.7], [0.0, 1.0], [0.0, 1.0]]
B = [[0.4, 0.7], [0.0, 1.0], [0.6, 0.9], [0.4, 0.8], [1.0, 1.0], [1.0, 1.0]]
C = [[1.0, 1.0], [0.0, 1.0], [0.9, 0.9], [0.0, 1.0], [1.0, 1.0], [1.0, 1.0]]
D = [[0.4, 0.7], [0.2, 1.0], [0.2, 1.0], [0.4, 0.8], [0.5, 1.0], [0.5, 0.8]]
E = [[0.5, 0.6], [0.5, 1.0], [0.6, 0.8], [0.5, 0.9], [0.8, 1.0], [0.8, 1.0]]

# Negacja przedziału
def negation(interval):
    return [1 - interval[1], 1 - interval[0]]

# Agregacja
def aggregation(x, y):
    return [(x[0] + y[0]) / 2, (x[1] + y[1]) / 2]

# Miara pierwszeństwa
def precedence(x, y):
    if x == y:
        return [1 - (x[1] - x[0]), 1]
    elif x[1] <= y[0]:
        return [0, 1]
    else:
        l = (1 - (x[1] - y[0])) / 2
        u = (1 - (x[0] - y[1])) / 2
        return [l, u]

# Miara podobieństwa
def similarity(A, AN):
    s_values = []
    for a, an in zip(A, AN):
        prec_1 = precedence(a, an)
        prec_2 = precedence(an, a)
        s = min(prec_1[0], prec_2[0]), min(prec_1[1], prec_2[1])
        s_values.append(s)
    return s_values

# Entropia
def entropy(set_intervals):
    negated_intervals = [negation(interval) for interval in set_intervals]
    s_values = similarity(set_intervals, negated_intervals)
    e_value = np.mean([sum(s) / 2 for s in s_values])
    return e_value

# Obliczenie entropii dla każdego obiektu
objects = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E}

entropies = {obj_name: entropy(obj_intervals) for obj_name, obj_intervals in objects.items()}

# Sortowanie wyników
sorted_entropies = sorted(entropies.items(), key=lambda item: item[1])

# Wyświetlenie wyników
for obj_name, ent_value in sorted_entropies:
    print(f"Entropia dla obiektu {obj_name}: {ent_value:.4f}")
