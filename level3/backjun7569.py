import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())

tomato_box = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
tomato_dq = deque()
#       [h][n][m]
# left  [x][x][-1]
# right [x][x][1]
# north [x][-1][x]
# south [x][1][x]
# up    [-1][x][x]
# down  [1][x][x]
def isValidated(nm, nn, nh):
    return 0 <= nm < M and 0 <= nn < N and 0 <= nh < H
def BFS():
    global tomato_dq, tomato_box, day
    directions = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

    while tomato_dq:
        m, n, h, day = tomato_dq.popleft()
        for dm, dn, dh in directions:
            nm, nn, nh = m + dm, n + dn, h + dh
            if isValidated(nm, nn, nh):
                if tomato_box[nh][nn][nm] == 0:
                    tomato_box[nh][nn][nm] = 1
                    tomato_dq.append((nm, nn, nh, day+1))
    return day

day = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato_box[h][n][m] == 1:
                tomato_dq.append((m, n, h, day))
day = BFS()
cannot_complete = False
for h in range(H):
    for n in range(N):
        for m in range(M):
            if tomato_box[h][n][m] == 0:
                cannot_complete = True
if cannot_complete:
    print(-1)
else:
    print(day)