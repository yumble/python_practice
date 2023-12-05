def isValidated(y, x):
    global visited
    return 0 <= y < n and 0 <= x < m and not visited[y][x]

def dfs(y, x, count, ans):
    global result
    global d
    if result >= ans + max_val * (4 - count):
        return
    if count == 4:
        result = max(result, ans)
        return
    for dy, dx in d:
        ny = y + dy
        nx = x + dx
        if isValidated(ny, nx):
            if count == 2: #'ㅗ' 모양 때문에 필요
                visited[ny][nx] = 1
                dfs(y, x, count + 1, ans + T[ny][nx])
                visited[ny][nx] = 0
            visited[ny][nx] = 1
            dfs(ny, nx, count + 1, ans + T[ny][nx])
            visited[ny][nx] = 0


n, m = map(int, input().split())
T = [list(map(int, input().split())) for _ in range(n)]
d = [(1,0), (-1,0), (0,1), (0,-1)]
visited = [[0] * m for _ in range(n)]
result = 0
max_val = max(map(max, T))
for y in range(n):
    for x in range(m):
        visited[y][x] = 1
        dfs(y, x, 1, T[y][x])
        visited[y][x] = 0
print(result)