# 나의 풀이
#
# import sys
#
# input = sys.stdin.readline
#
# n, m = map(int, input().split())
#
# board = [input() for _ in range(n)]
#
# def searchBoard(color):
#     min_num = 64
#     for i in range(n-7):
#         for j in range(m-7):
#             tmp = 0
#             for k in range(8):
#                 for o in range(8):
#                     if (k % 2 == 0 and o % 2 == 0) or (k % 2 == 1 and o % 2 == 1):
#                         if board[i + k][j + o] != color:
#                             tmp += 1
#                     elif (k % 2 == 0 and o % 2 == 1) or (k % 2 == 1 and o % 2 == 0):
#                         if board[i + k][j + o] == color:
#                             tmp += 1
#             min_num = min_num if min_num < tmp else tmp
#     return min_num
#
# blackNum = searchBoard('B')
# whiteNum = searchBoard('W')
# print(blackNum if blackNum < whiteNum else whiteNum)

import sys
input = sys.stdin.readline
n, m = map(int, input().split())
board = [input() for _ in range(n)]
ans = 64
def fill(y,x,color):
    global ans
    cnt = 0
    for i in range(8):
        for j in range(8):
            if (i+j) % 2 :
                if board[y+i][x+j] == color:
                    cnt += 1
            else:
                if board[y+i][x+j] != color:
                    cnt += 1
    ans = min(ans, cnt)

for i in range(n-7):
    for j in range(m-7):
        fill(i,j,'B')
        fill(i,j,'W')

print(ans)