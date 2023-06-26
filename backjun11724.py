import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n, m = map(int, input().split())

adj = [[0] * (n+1) for _ in range(n+1)]
chk = [False] * (n+1)
ans = 0

for _ in range(m):
    a, b = map(int, input().split())
    adj[a][b] = adj[b][a] = 1

def dfs(now):
    #chk[nxt] = True next로 와서 체크하는 방식 (비추천)
    for nxt in range(n+1):
        if adj[now][nxt] and not chk[nxt]:
            chk[nxt] = True # next 가기전에 체크하는 방식
            dfs(nxt)


for i in range(1, n+1):
    if not chk[i]:
        ans += 1
        chk[i] = True
        dfs(i)

print(ans)
