from collections import deque

N, M = map(int, input().split())

ladders = dict()
for _ in range(N):
    a,b = map(int, input().split())
    ladders[a] = b
snakes = dict()
for _ in range(M):
    a,b = map(int, input().split())
    snakes[a] = b
# snakes = [tuple(map(int, input().split())) for _ in range(M)]

isVisited = [False] * 120
dq = deque()
dq.append((1,0))
isVisited[1] = True

min_result = 200
while dq:
    position, count = dq.popleft()
    for i in range(1, 7, 1):
        if position + i <= 100 and not isVisited[position + i]:
            next_position = position + i
            if ladders.get(next_position):
                next_position = ladders[next_position]
            if snakes.get(next_position):
                next_position = snakes[next_position]
            if not isVisited[next_position]:
                isVisited[next_position] = True
                dq.append((next_position, count + 1))
            if next_position == 100:
                min_result = min(min_result, count + 1)


print(min_result)