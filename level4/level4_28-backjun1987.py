def isValidated(nr, nc, alphabets):
    return 0 <= nr < R and 0 <= nc < C and board[nr][nc] not in alphabets
def BFS(r, c):
    global board

    dq = set()
    alphabets = board[r][c]
    dq.add((r, c, alphabets))
    result = 1

    while dq:
        r, c, alphabets = dq.pop()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if isValidated(nr, nc, alphabets):
                dq.add((nr, nc, alphabets + board[nr][nc]))
                result = max(result, len(alphabets)+1)
    return result


R, C = map(int, input().split())

board = [list(input()) for _ in range(R)]


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

print(BFS(0, 0))
