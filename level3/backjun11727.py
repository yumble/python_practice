#DP

def dp(n):
    global results
    if n == 1:
        return 1
    elif n == 2:
        return 3
    else:
        if results[n]:
            return results[n]
        results[n] = (dp(n-1) + 2 * dp(n-2)) % 10007
        return results[n]

n = int(input())
results = [0] * (n+1)
print(dp(n))