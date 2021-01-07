"""
2020 = a + b + c
2020 - a = b + c
"""

from itertools import combinations

def solve(arr):
    for a, b in combinations(arr, 2):
        c = 2020 - (a + b)
        if c in arr:
            return a * b * c
    

reports = open("./input", "r").read().split()
reports = list(map(lambda x: int(x), reports))
print(solve(reports))
