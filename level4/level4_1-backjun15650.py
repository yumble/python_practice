# dfs or combination
from itertools import combinations

n, m = map(int, input().split())

for a in combinations(range(1,n+1), m):
    # print(" ".join(map(str, a)))
    print(*a)
