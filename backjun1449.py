import sys

input = sys.stdin.readline

n, l = map(int, input().split())

holes = list(map(int, input().split()))
holes.sort()

tapeCount = 1
tapeStart = holes[0] + l - 1

for hole in holes:
    if tapeStart >= hole:
        continue
    tapeStart = hole + l - 1
    tapeCount += 1

print(tapeCount)

## Ver 2
# N,L = map(int, input().split())
# coord = [False] * 1001
# for i in map(int, input().split()):
#     coord[i] = True
#
# ans = 0
# x = 0
# while x < 1001:
#     if coord[x]:
#         ans += 1
#         x += L
#     else:
#         x += 1
# print(ans)