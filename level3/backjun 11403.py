from collections import deque
n = int(input())

graph = [list(map(int, input().split())) for _ in range(n)]

#플로이드 워셜 알고리즘 N^3
# 100 * 100 * 100 = 1000000 충분히 가능

for k in range(n):
    for i in range(n):
        for j in range(n):
            if graph[i][k] and graph[k][j]:
                graph[i][j] = 1

for row in graph:
    print(' '.join(map(str, row)))