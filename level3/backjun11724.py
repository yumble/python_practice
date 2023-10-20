from collections import deque

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
chk = [False] * (n + 1)
connect = 0
for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bfs(i):
    global chk
    dq = deque([i])
    while dq:
        num = dq.popleft()
        for n in graph[num]:
            if not chk[n]:
                dq.append(n)
                chk[n] = True

for i in range(1, n + 1):
    if not chk[i]:
        connect += 1
        bfs(i)
print(connect)
