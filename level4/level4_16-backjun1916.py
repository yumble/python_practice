import heapq  # 우선순위 큐 구현을 위함
import sys
input = sys.stdin.readline

n = int(input())
m = int(input())

arr = [{} for _ in range(n+1)]
for _ in range(m):
    origin, destination, cost = map(int, input().split())
    if destination in arr[origin]:
        arr[origin][destination] = min(arr[origin][destination], cost)
    else:
        arr[origin][destination] = cost
def dijkstra(arr, start, end):
    distances = [100_000_000] * len(arr)
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (distances[start], start))

    while queue:
        distance, now = heapq.heappop(queue)

        if distances[now] < distance:
            continue

        for new, new_distance in arr[now].items():
            new_distance += distance
            if new_distance < distances[new]:
                distances[new] = new_distance
                heapq.heappush(queue, (new_distance, new))
    print(distances[end])

start, end = map(int, input().split())
dijkstra(arr, start, end)