# cache = [[0] * 10 for _ in range(102)]
#
# mod = 1_000_000_000
# cache[1][0] = 0
# cache[1][1] = 1
# cache[1][2] = 1
# cache[1][3] = 1
# cache[1][4] = 1
# cache[1][5] = 1
# cache[1][6] = 1
# cache[1][7] = 1
# cache[1][8] = 1
# cache[1][9] = 1
#
# for i in range(2, 101):
#     cache[i][0] = cache[i-1][1]
#     cache[i][1] = (cache[i-1][2] + cache[i-1][0]) % mod
#     cache[i][2] = (cache[i-1][1] + cache[i-1][3]) % mod
#     cache[i][3] = (cache[i-1][2] + cache[i-1][4]) % mod
#     cache[i][4] = (cache[i-1][3] + cache[i-1][5]) % mod
#     cache[i][5] = (cache[i-1][4] + cache[i-1][6]) % mod
#     cache[i][6] = (cache[i-1][5] + cache[i-1][7]) % mod
#     cache[i][7] = (cache[i-1][6] + cache[i-1][8]) % mod
#     cache[i][8] = (cache[i-1][7] + cache[i-1][9]) % mod
#     cache[i][9] = cache[i-1][8]
# print(sum(cache[int(input())]) % mod)
#

mod = 1_000_000_000

cache = [[0]*10 for _ in range(101)]
for j in range(1,10):
    cache[1][j] = 1
for i in range(2,101):
    for j in range(10):
        if j > 0:
            cache[i][j] += cache[i-1][j-1]
            cache[i][j] %= mod
        if j < 9:
            cache[i][j] += cache[i-1][j+1]
            cache[i][j] %= mod

ans = 0
n = int(input())
for j in range(10):
    ans += cache[n][j]
    ans %= mod
print(ans)