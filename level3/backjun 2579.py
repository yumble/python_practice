import sys
input = sys.stdin.readline

n = int(input())
stairs = [int(input()) for _ in range(n)]

dp = [-1] * (n+1)
dp[1] = stairs[0]
if n > 1:
    dp[2] = stairs[0] + stairs[1]
if n > 2:
    dp[3] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])

for i in range(4, n+1):
    dp[i] = stairs[i-1] + max( dp[i-2], stairs[i-2] + dp[i-3] )
print(dp[n])