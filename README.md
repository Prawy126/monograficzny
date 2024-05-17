# PROJEKT GRUPA 5

```python
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


def part_order(x, y):
    if x[0] <= y[0] and x[1] <= y[1]:
        return True
    return False


# Miara pierwszeństwa
def precedence(x, y):
    if x == y:
        return [1 - (x[1] - x[0]), 1]
    elif part_order(x, y):
        return [1, 1]
    else:
        l = (1 - x[1] + y[0]) / 2
        u = (1 - x[0] + y[1]) / 2
        return [l, u]


# Miara podobieństwa
def similarity(A, AN):
    s_values = []
    for a, an in zip(A, AN):
        prec_1 = precedence(a, an)
        prec_2 = precedence(an, a)
        # (f"Prec1:{prec_1} Prec2:{prec_2} |\n")
        s = min(prec_1[0], prec_2[0]), min(prec_1[1], prec_2[1])
        s_values.append(s)
    print("------------------------------")
    return s_values


def mean_interval(interval1, interval2):
    """
    Calculates the mean interval of two intervals.
    """
    return [(interval1[0] + interval2[0]) / 2, (interval1[1] + interval2[1]) / 2]


def process_intervals(intervals):
    """
    Processes a list of intervals using the mean_interval function until only one interval remains.
    """
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

    return intervals[0]


# Define the list of intervals
A = [[0.0, 1.0], [0.5, 1.0], [0.6, 0.8], [0.4, 0.7], [0.0, 1.0]]

AN = [negation(interval) for interval in A]
BN = [negation(interval) for interval in B]
CN = [negation(interval) for interval in C]
DN = [negation(interval) for interval in D]
EN = [negation(interval) for interval in E]

print("Wynik dla  zbioru A ")
print(process_intervals(similarity(A,AN)))
print("\n\nWynik dla  zbioru B")
print(process_intervals(similarity(B,BN)))
print("\n\nWynik dla  zbioru C")
print(process_intervals(similarity(C,CN)))
print("\n\nWynik dla  zbioru D")
print(process_intervals(similarity(D,DN)))
print("\n\nWynik dla  zbioru E")
print(process_intervals(similarity(E,EN)))



```