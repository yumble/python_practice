cache= [0] * 10001
cache[1] = 1
cache[2] = 2
n = int(input())
mod = 10007

def dp(n):
    if n == 1:
        return cache[1]
    elif n == 2:
        return cache[2]
    else:
        if cache[n]:
            return cache[n]
        cache[n] = dp(n-1) + dp(n-2)
        cache[n] %= mod
    return cache[n]

print(dp(n))