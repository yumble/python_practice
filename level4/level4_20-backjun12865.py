import sys

input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[0] * (K + 1) for _ in range(N + 1)] # 가로 무게 1~K, 세로 입력한 횟수

for i in range(1, N + 1):
    w, v = map(int, input().split())
    for j in range(1, K + 1):
        if w > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)

print(dp[N][K])
