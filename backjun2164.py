import sys
from collections import deque

# 배열은 맨 앞 삭제, 맨 앞의 값 맨 뒤로 -> O(N)
# 1개만 남겨야하므로 총 N-1번 수행
# -> O(N^2) 시간 초과
# => 큐를 이용하자 삽입,삭제 O(1) * N

dq = deque(range(1, int(sys.stdin.readline())+1))

while len(dq) != 1:
    dq.popleft()
    dq.append(dq.popleft())

print(dq.popleft())
