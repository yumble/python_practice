import sys
sys.setrecursionlimit(1000000)

dx = (1, 0, -1, 0)
dy = (0, 1, 0, -1)


def check_cabbage(ground, k):
    cabbage_list = []
    for _ in range(k):
        x, y = map(int, input().split())
        ground[y][x] = True
        cabbage_list.append((x, y))
    return cabbage_list

def isValidCoord(ny, nx):
    global m, n
    return 0 <= ny < n and 0 <= nx < m

def dfs(x, y):
    global is_visited, ground
    if is_visited[y][x]:
        return
    is_visited[y][x] = True
    for k in range(4):
        ny = y + dy[k]
        nx = x + dx[k]
        if isValidCoord(ny, nx) and not is_visited[ny][nx] and ground[ny][nx]:
            dfs(nx, ny)


test = int(input())
for _ in range(test):
    m, n, k = map(int, input().split())
    bug = 0
    ground = [[False] * m for _ in range(n)]
    is_visited = [[False] * m for _ in range(n)]
    cabbage_list = check_cabbage(ground, k)
    for x, y in cabbage_list:
        if not is_visited[y][x]:
            bug += 1
            dfs(x, y)

    print(bug)

