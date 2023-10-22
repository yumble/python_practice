import sys
sys.setrecursionlimit(1000000)

n, m = map(int, input().split())
university = []
visited = [[False] * m for _ in range(n)]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
count = 0
for _ in range(n):
    university.append(list(input()))


def check_i_position():
    global university
    return next((y, x) for y, row in enumerate(university) for x, val in enumerate(row) if val == 'I')


def is_validated(y, x):
    return 0 <= y < n and 0 <= x < m


def dfs(y, x):
    global university, count
    visited[y][x] = True
    if university[y][x] == 'P':
        count += 1
    if university[y][x] == 'X':
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if is_validated(ny, nx) and not visited[ny][nx]:
            dfs(ny, nx)


y, x = check_i_position()
dfs(y, x)
print(count if count != 0 else "TT")
