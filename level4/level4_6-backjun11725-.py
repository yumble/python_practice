from collections import deque

n = int(input())
tree = [[] for _ in range(n+1)]
parent = [0] * (n+1)
visited = [False] * (n+1)
dq = deque()

for _ in range(n-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

dq.append(1)
visited[1] = True

while dq:
    node = dq.popleft()
    for child in tree[node]:
        if not visited[child]:
            dq.append(child)
            parent[child] = node
            visited[child] = True

print('\n'.join(map(str,parent[2:])))
