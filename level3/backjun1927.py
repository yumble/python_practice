import heapq
import sys
input = sys.stdin.readline

n = int(input())

heap = []
for _ in range(n):
    m = int(input())
    if m == 0:
        if len(heap) != 0:
            print(heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, m)