import heapq
import sys

input = sys.stdin.readline

def dijkstra(start, end):
    distance = [float('inf')] * (N + 1)
    distance[start] = 0
    queue = [(start, 0)]
    while queue:
        now, dist = heapq.heappop(queue)
        if distance[now] < dist:
            continue

        for u, d in graph[now]:
            if d != -1 and distance[u] > distance[now] + d:
                distance[u] = distance[now] + d
                heapq.heappush(queue, (u, distance[u]))
    return distance[end]


N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())
result = min(dijkstra(1, v1) + dijkstra(v1, v2) + dijkstra(v2, N),
           dijkstra(1, v2) + dijkstra(v2, v1) + dijkstra(v1, N))
print(result if result < float('inf') else -1)