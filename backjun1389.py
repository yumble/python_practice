import sys
from collections import deque
import time

input = sys.stdin.readline

n, m = map(int, input().split())

adj = [ [0] * n for _ in range(n) ]

for _ in range(m):
    a, b = map(lambda x : x-1, map(int, input().split()))
    adj[a][b] = 1
    adj[b][a] = 1
# print(f'adj {adj}')

def check(checked):
    boolean = True
    for chk in checked:
        if chk == False:
            boolean = False
            break
    return boolean
def bfs(i):
    count = 0
    distance = [0] * n
    checked = [False] * n
    checked[i] = True
    dq = deque()
    dq.append((i,count))

    while dq:
        tot_chk = False
        now, now_count = dq.popleft()
        # print(f'now {now}')
        now_distance = now_count + 1
        for nxt in range(n):
            # print(f'distance {distance}')
            # print(f'checked {checked}')
            if check(checked):
                return sum(distance)
            if checked[nxt]:
                continue
            if adj[now][nxt]:
                # print(f'nxt {nxt}')
                checked[nxt] = True
                dq.append((nxt, now_distance))
                if not distance[nxt]:
                    distance[nxt] = now_distance

    return sum(distance)

min_num = (-1, 10000)

for i in range(n):
    a = bfs(i)
    # print(f'i {i} a {a}')
    min_num = (i, a) if min_num[1] > a else min_num

print(min_num[0]+1)
