import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
dy = (0, 1, 0, -1)
dx = (1, 0, -1, 0)
board = [input() for _ in range(N)]

def isValidCoord(y, x):
    return 0 <= y < N and 0 <= x < M


def bfs():
    chk = [[False] * M for _ in range(N)]
    chk[0][0] = True
    q = deque()
    q.append((0, 0, 1))
    while q:
        y, x, d = q.popleft()

        if y == N-1 and x == M-1:
            return d
        nd = d + 1
        for k in range(4):
            ny = y + dy[k]
            nx = x + dx[k]
            if isValidCoord(ny, nx) and board[ny][nx] == '1' and not chk[ny][nx]:
                chk[ny][nx] = True
                q.append((ny, nx, nd))
    return -1

print(bfs())