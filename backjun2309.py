import sys
from itertools import combinations

input = sys.stdin.readline

v = [int(input()) for _ in range(9)]

for i in combinations(v,7):
    if sum(i) == 100:
        for j in sorted(i):
            print(j)
        break