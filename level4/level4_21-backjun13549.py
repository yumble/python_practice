from collections import deque

N, M = map(int, input().split())
memory = [-1] * 100001

dp = deque()
dp.append(N)
memory[N] = 0

def validate(n):
    return 0 <= n <= 100000
def bfs():
    while dp:
        now = dp.popleft()

        if memory[M] != -1:
            break

        if validate(now * 2) and memory[now * 2] == -1:
            dp.appendleft(now * 2)
            memory[now * 2] = memory[now]

        if validate(now - 1) and memory[now - 1] == -1:
            dp.append(now - 1)
            memory[now - 1] = memory[now] + 1

        if validate(now + 1) and memory[now + 1] == -1:
            dp.append(now + 1)
            memory[now + 1] = memory[now] + 1

bfs()
print(memory[M])

