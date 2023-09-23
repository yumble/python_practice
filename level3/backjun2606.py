# 그냥 BFS,DFS..?
from collections import deque

queue = deque()
n = int(input())
matrix = [[0] * (n+1) for _ in range(n+1)]
visited = [0] * (n+1)

m = int(input())
for _ in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = 1
    matrix[b][a] = 1

queue.append(1)
num_set = set()
while queue:
    now = queue.popleft()
    for i in range(1, n+1):
        if matrix[now][i] and not visited[i]:
            queue.append(i)
            num_set.add(i)
            visited[i] = 1
if 1 in num_set:
    num_set.remove(1)
print(len(num_set))