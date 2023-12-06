# dfs or combination
from itertools import combinations_with_replacement as cwr

n, m = map(int, input().split())

for a in cwr(range(1,n+1), m):
    # print(" ".join(map(str, a)))
    print(*a)
