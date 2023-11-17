import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())

tomato_box = [list(map(int, input().split())) for _ in range(N)]
tomato_dq = deque()

def isValidated(nm, nn):
    return 0 <= nm < M and 0 <= nn < N

def BFS():
    global tomato_dq, tomato_box, day
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    while tomato_dq:
        m, n, day = tomato_dq.popleft()
        for dm, dn in directions:
            nm, nn = m + dm, n + dn
            if isValidated(nm, nn):
                if tomato_box[nn][nm] == 0:
                    tomato_box[nn][nm] = 1
                    tomato_dq.append((nm, nn, day + 1))
    return day


day = 0
for n in range(N):
    for m in range(M):
        if tomato_box[n][m] == 1:
            tomato_dq.append((m, n, day))
day = BFS()
cannot_complete = False
for n in range(N):
    for m in range(M):
        if tomato_box[n][m] == 0:
            cannot_complete = True
if cannot_complete:
    print(-1)
else:
    print(day)
