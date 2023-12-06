# dfs or combination
from itertools import permutations

n, m = map(int, input().split())

arr = list(map(int, input().split()))
arr.sort()

for a in permutations(arr, m):
    print(*a)
