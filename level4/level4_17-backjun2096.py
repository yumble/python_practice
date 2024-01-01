import sys

input = sys.stdin.readline

n = int(input())
dp = list(map(int, input().split()))

max_dp = dp[:]
min_dp = dp[:]
tmp_max_dp = [0,0,0]
tmp_min_dp = [0,0,0]

for i in range(1, n):
    dp = list(map(int, input().split()))

    tmp_max_dp[0] = dp[0] + max(max_dp[0], max_dp[1])
    tmp_max_dp[1] = dp[1] + max(max_dp[0], max_dp[1], max_dp[2])
    tmp_max_dp[2] = dp[2] + max(max_dp[1], max_dp[2])

    tmp_min_dp[0] = dp[0] + min(min_dp[0], min_dp[1])
    tmp_min_dp[1] = dp[1] + min(min_dp[0], min_dp[1], min_dp[2])
    tmp_min_dp[2] = dp[2] + min(min_dp[1], min_dp[2])

    max_dp = tmp_max_dp[:]
    min_dp = tmp_min_dp[:]

print(f"{max(max_dp)} {min(min_dp)}")