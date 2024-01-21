import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)
def dijkstra(start):
    distance[start] = 0
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        dist, now = heapq.heappop(queue)
        if distance[now] < dist:
            continue

        for u, d in graph[now]:
            if distance[u] > distance[now] + d:
                distance[u] = distance[now] + d
                heapq.heappush(queue, (distance[u], u))
    return distance


V, E = map(int, input().split())
S = int(input())
graph = [[] for _ in range(V + 1)]
distance = [INF] * (V + 1)
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

result = dijkstra(S)
for i in range(1, V + 1):
    print(result[i] if result[i] != INF else 'INF')
