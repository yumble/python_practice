T = int(input())

def get_max_score():
    n = int(input())
    dp = list(list(map(int, input().split())) for _ in range(2))

    if n == 1:
        return max(dp[0][0], dp[1][0])

    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]

    for i in range(2, n):
        dp[0][i] = max(dp[1][i-1], dp[1][i-2]) + dp[0][i]
        dp[1][i] = max(dp[0][i-1], dp[0][i-2]) + dp[1][i]
    return max(dp[0][n-1], dp[1][n-1])

for _ in range(T):
    print(get_max_score())

