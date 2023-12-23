from collections import deque

n, m = map(int, input().split())
visited = 50
def bfs(n):
    global visited
    dq = deque()
    dq.append((n, 1))
    while dq:
        now, count = dq.popleft()
        if now == m:
            visited = min(visited, count)
        if now * 2 > m:
            continue
        else:
            dq.append(((now*2), count + 1))
        if now * 10 + 1 > m:
            continue
        else:
            dq.append(((now * 10 + 1), count + 1))

bfs(n)
print(visited if visited != 50 else -1)