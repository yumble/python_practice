# ver 1 BFS
from collections import deque

def min_operations_to_one(N):
    queue = deque([(N, 0)])  # (현재 숫자, 연산 횟수)

    while queue:
        num, ops = queue.popleft()

        if num == 1:
            return ops

        if num % 3 == 0:
            queue.append((num // 3, ops + 1))
        if num % 2 == 0:
            queue.append((num // 2, ops + 1))
        queue.append((num - 1, ops + 1))

N = int(input())
result = min_operations_to_one(N)
print(result)
