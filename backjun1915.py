# dp
# D(i,j) : i,j 칸을 우하단으로하는 정사각형 최대 크기
import sys
input = sys.stdin.readline

n, m = map(int,input().split())
arr = [input() for _ in range(n)]
aa = [[0] * m for _ in range(n)]

def dp(i,j):
    if arr[i][j] == '0':
        return 0
    if i == 0 or j == 0:
        aa[i][j] = int(arr[i][j])
        return aa[i][j]
    aa[i][j] = min(aa[i-1][j-1], aa[i-1][j], aa[i][j-1]) + 1
    return aa[i][j]


max_num = 0
for i in range(n):
    for j in range(m):
        max_num = max(max_num, dp(i,j))

print(max_num**2)

# for j in range(m):
#     if arr[0][j] == '1':
#         aa[0][j] = 1
# for i in range(n):
#     if arr[i][0] == '1':
#         aa[i][0] = 1
#     for j in range(1,m):
#         if arr[i][j] == '1':
#             aa[i][j] = min(aa[i][j-1], aa[i-1][j], aa[i-1][j-1]) +1
#
# ans = 0
# for i in range(n):
#     for j in range(m):
#         ans = max(ans, aa[i][j])