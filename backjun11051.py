import sys
sys.setrecursionlimit(10**7)

n, k = map(int,input().split())
mod = 10007
cache = [ [0] * 1001 for _ in range(1001)]

def bino(n, k):
    if cache[n][k] :
        return cache[n][k]

    if k == 0 or k == n :
        cache[n][k] = 1
    else:
        cache[n][k] = bino(n - 1, k - 1) + bino( n - 1, k)
        # 캐시에 저장할때도 나머지만 저장하자
        cache[n][k] %= mod
    return cache[n][k]

print(bino(n,k))

# for문
for i in range(1001):
    cache[i][0] = cache[i][i] = 1
    for j in range(1,i): # 0, i는 위에서 처리, 1~i-1만 처리하면됨
        cache[i][j] = cache[i-1][j-1] + cache[i-1][j]
        cache[i][j] %= mod

print(cache[n][k])