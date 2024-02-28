from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited_node = [False] * (n+1)
for _ in range(m):
    i, j = map(int,input().split())
    graph[i].append(j)
    graph[j].append(i)
for sorts in graph:
    sorts.sort()

def dfs(v):
    print(v, end = ' ')
    visited_node[v] = True
    for i in graph[v]:
        if not visited_node[i]:
            dfs(i)
def bfs(v):
    q = deque()
    q.append(v)
    visited_node[v] = True
    while q:
        v = q.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not visited_node[i]:
                q.append(i)
                visited_node[i] =True
dfs(v)
print()
visited_node = [False] * (n+1)
bfs(v)