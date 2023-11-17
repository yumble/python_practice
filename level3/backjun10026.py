import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

color_box = [list(map(str,input().strip())) for _ in range(n)]
visited = [[0] * n for _ in range(n) ]
dq = deque()
directions = [ (0,1), (0,-1), (1,0), (-1,0)]
block = 0
def isValidated(x, y):
    return 0 <= x < n and 0 <= y < n and not visited[x][y]
def BFS():
    global block, color_box, visited
    block += 1
    while dq:
        x, y = dq.popleft()
        block_color = color_box[x][y]
        visited[x][y] = block
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if isValidated(nx, ny) and color_box[nx][ny] == block_color :
                visited[nx][ny] = block
                dq.append((nx, ny))

def count_block():
    global visited
    return max(max(row) for row in visited)

# 적목색맹이 아닌 경우
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dq.append((i,j))
            BFS()
a = count_block()

# 초기화
dq = deque()
visited = [[0] * n for _ in range(n) ]
block = 0
# 적목색맹인 경우를 위해 G를 R로 변경
for i in range(n):
    for j in range(n):
        if color_box[i][j] == 'G':
            color_box[i][j] = 'R'
# 적목색맹인 경우
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dq.append((i,j))
            BFS()

b = count_block()

print(f'{a} {b}')