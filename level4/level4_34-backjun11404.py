INF = int(1e9)

n = int(input())
m = int(input())

dist = [[INF] * n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0
for _ in range(m):
    a, b, c = map(int, input().split())
    dist[a - 1][b - 1] = min(dist[a - 1][b - 1], c)

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

for i in range(n):
    for j in range(n):
        if dist[i][j] == INF:
            print(0, end=' ')
            continue
        print(dist[i][j], end=' ')
    print()