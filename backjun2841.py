import sys

input = sys.stdin.readline

n, p = map(int, input().split())

guitar = [[] for _ in range(7)]
ans = 0

for _ in range(n):
    l, plat = map(int, input().split())

    while guitar[l] and guitar[l][-1] > plat:
        guitar[l].pop()
        ans += 1

    if guitar[l] and guitar[l][-1] == plat:
        continue
    guitar[l].append(plat)
    ans += 1

print(ans)
