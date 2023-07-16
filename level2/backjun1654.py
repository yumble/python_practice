import sys
input = sys.stdin.readline

k, n = map(int, input().split())

lines = []
for _ in range(k):
    lines.append(int(input()))

start = 1
end = max(lines)

while start <= end:
    cnt = 0
    mid = (start + end) // 2
    for line in lines:
        if line >= mid:
            cnt += line // mid
    if n > cnt:
        end = mid - 1
    else:
        result = mid #📌!!!!!!!!!!!!!!!
        start = mid + 1

print(result)