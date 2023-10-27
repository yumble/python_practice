from collections import deque

n, k = map(int, input().split())
distance = [0] * 100001
dq = deque()
dq.append(n)

def bfs():
    while dq:
        position = dq.popleft()
        if position == k:
            return distance[k]
        for new in (position-1, position+1, position*2):
            if 0 <= new <= 100000 and not distance[new]:
                distance[new] = distance[position] + 1
                dq.append(new)
print(bfs())