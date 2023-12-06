# dfs or combination
from itertools import combinations_with_replacement as cwr

n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

for a in cwr(arr, m):
    print(*a)
