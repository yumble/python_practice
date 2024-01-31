from collections import deque
import sys

input = sys.stdin.readline

n = int(input())

tree = [[] for _ in range(n+1)]

for _ in range(n-1):
    a, b, c = map(int, input().split())
    tree[a].append((b, c))
    tree[b].append((a, c))

def BFS(start):
    dq = deque()
    dq.append((start, 0))
    visited = [-1] * (n+1)
    visited[start] = 0
    while dq:
        node, distance = dq.popleft()
        for next, next_distance in tree[node]:
            if visited[next] == -1:
                visited[next] = next_distance + distance
                dq.append((next, next_distance + distance))
    return (visited.index(max(visited)), max(visited))

print(BFS(BFS(1)[0])[1])