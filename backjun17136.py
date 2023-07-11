import sys
input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(10)]
ans = 25
paper = [0] * 6 #사용한 색종이 개수

def is_possible(y,x,sz):
    if paper[sz] == 5:
        return False

    if y + sz > 10 or x+sz>10:
        return False

    for i in range(sz):
        for j in range(sz):
            if board[y+i][x+j] == 0:
                return False
    return True

def mark(y, x, sz, value):
    for i in range(sz):
        for j in range(sz):
            board[y+i][x+j] = value
    if value:
        paper[sz] -= 1
    else:
        paper[sz] += 1


def backtracking(y,x):
    global ans
    if y == 10:
        ans = min(ans, sum(paper))
        return
    if x == 10:
        backtracking(y+1, 0)
        return
    if board[y][x] == 0:
        backtracking(y, x+1)
        return
    # board[y][x]가 1인경우만 여기까지 나온다.
    for sz in range(1, 6):
        if is_possible(y, x, sz):
            mark(y, x, sz, 0)
            backtracking(y, x+1)
            mark(y, x, sz, 1)

backtracking(0, 0)
print(-1 if ans == 25 else ans)