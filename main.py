import numpy as np

# Definicja przedziałowych zbiorów rozmytych
A = [[0.0, 1.0], [0.5, 1.0], [0.6, 0.8], [0.4, 0.7], [0.0, 1.0], [0.0, 1.0]]
B = [[0.4, 0.7], [0.0, 1.0], [0.6, 0.9], [0.4, 0.8], [1.0, 1.0], [1.0, 1.0]]
C = [[1.0, 1.0], [0.0, 1.0], [0.9, 0.9], [0.0, 1.0], [1.0, 1.0], [1.0, 1.0]]
D = [[0.4, 0.7], [0.2, 1.0], [0.2, 1.0], [0.4, 0.8], [0.5, 1.0], [0.5, 0.8]]
E = [[0.5, 0.6], [0.5, 1.0], [0.6, 0.8], [0.5, 0.9], [0.8, 1.0], [0.8, 1.0]]


# Negacja przedziału
def negation(interval):
    return [round(1 - interval[1], 4), round(1 - interval[0], 4)]


# Agregacja
def aggregation(x, y):
    return [round((x[0] + y[0]) / 2, 4), round((x[1] + y[1]) / 2, 4)]


def part_order(x, y):
    if x[0] <= y[0] and x[1] <= y[1]:
        return True
    return False


# Miara pierwszeństwa
def precedence(x, y):
    if x == y:
        return [round(1 - (x[1] - x[0]), 4), 1]
    elif part_order(x, y):
        return [1, 1]
    else:
        l = round((1 - x[1] + y[0]) / 2, 4)
        u = round((1 - x[0] + y[1]) / 2, 4)
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


def mean_interval(interval1, interval2):
    """
    Calculates the mean interval of two intervals.
    """
    return [round((interval1[0] + interval2[0]) / 2, 4), round((interval1[1] + interval2[1]) / 2, 4)]


def process_intervals(intervals, name):
    """
    Processes a list of intervals using the mean_interval function until only one interval remains.
    Prints the set name and iteration number for each iteration.
    """
    print(f"Zbiór {name}:")
    print("   Iteracja 0:", ", ".join(map(str, intervals)))  # Wyświetlenie początkowego zestawu przedziałów
    iteration = 1
    while len(intervals) > 1:
        result = []
        length = len(intervals)

        # Iterate over the intervals in pairs
        for i in range(0, length - 1, 2):
            result.append(mean_interval(intervals[i], intervals[i + 1]))

        # If the number of intervals is odd, carry the last unpaired interval to the next round
        if length % 2 != 0:
            result.append(intervals[-1])

        intervals = result

        # Print the set name and iteration number with indentation
        indentation = " " * (6 * (iteration - 1)) + " " * (3 * (iteration - 1))
        print(" " * 15, indentation, "Iteracja", iteration, ":", ", ".join(map(str, intervals)))

        iteration += 1

    return intervals[0]

# Pozostała część kodu bez zmian
AN = [negation(interval) for interval in A]
BN = [negation(interval) for interval in B]
CN = [negation(interval) for interval in C]
DN = [negation(interval) for interval in D]
EN = [negation(interval) for interval in E]

results = []

print("Wyniki dla zbiorów:")
result_A = process_intervals(similarity(A, AN), 'A')
results.append(('A', result_A))

result_B = process_intervals(similarity(B, BN), 'B')
results.append(('B', result_B))

result_C = process_intervals(similarity(C, CN), 'C')
results.append(('C', result_C))

result_D = process_intervals(similarity(D, DN), 'D')
results.append(('D', result_D))

result_E = process_intervals(similarity(E, EN), 'E')
results.append(('E', result_E))

# Sortowanie wyników według warunku x ≤ y
sorted_results = sorted(results, key=lambda x: x[1][0])

print("\nPosortowane wyniki:")
for name, interval in sorted_results:
    print(f"Zbiór {name}: {interval}")


