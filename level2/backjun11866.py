from collections import deque

n, m = map(int, input().split())

q = deque()
ans = []
for i in range(1, n+1):
    q.append(i)

while q:
    for _ in range(m-1):
        q.append(q.popleft())
    ans.append(q.popleft())

ans_str = ', '.join(map(str, ans))
print("<" + ans_str + ">")
