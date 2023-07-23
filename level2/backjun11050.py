from itertools import combinations
n, k = map(int, input().split())
ans = 1
for i in range(n, n-k, -1):
    ans *= i
for i in range(k, 0, -1):
    ans //= i

print(ans)