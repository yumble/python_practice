from collections import deque
N, M = map(int, input().split())

ground = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
ground_with_distance = [[0] * M for _ in range(N)]


dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def isValidated(x, y):
    return 0 <= x < N and 0 <= y < M and ground[x][y]

def bfs(x, y):
    dq = deque()
    dq.append((x, y, 0))
    visited[x][y] = 1
    while dq:
        x, y, distance = dq.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if isValidated(nx, ny) and not visited[nx][ny]:
                dq.append((nx, ny, distance + 1))
                visited[nx][ny] = 1
                ground_with_distance[nx][ny] = distance + 1

def find2Coordinate():
    for i in range(N):
        for j in range(M):
            if ground[i][j] == 2:
                return (i,j)
def checkMinus1():
    global ground_with_distance, ground
    for i in range(N):
        for j in range(M):
            if ground[i][j] and not ground_with_distance[i][j]:
                ground_with_distance[i][j] = -1

i, j = find2Coordinate()
bfs(i, j)
checkMinus1()
ground_with_distance[i][j] = 0

for row in ground_with_distance:
    print(' '.join(map(str, row)))