from collections import deque

N, K = map(int, input().split())

distance = [0] * 100001
queue = deque()
queue.append((N, 0))

min_path = 0
cnt = 0

while queue:
    now, count = queue.popleft()
    if now == K:
        min_path = count
        cnt += 1
        continue

    for nxt in [now - 1, now + 1, now * 2]:
        if 0 <= nxt <= 100000 and (distance[nxt] == 0 or distance[nxt] == count + 1):
            distance[nxt] = count + 1
            queue.append((nxt, count + 1))

print(min_path)
print(cnt)