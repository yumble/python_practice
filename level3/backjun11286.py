import heapq
import sys
input = sys.stdin.readline
min_hq = []
max_hq = []

n = int(input())
for _ in range(n):
    number = int(input())
    if number > 0:
        heapq.heappush(min_hq, number)
    elif number < 0:
        heapq.heappush(max_hq, -number)
    else:
        if min_hq:
            if max_hq:
                if(min_hq[0] < max_hq[0]):
                    print(heapq.heappop(min_hq))
                else: #절댓값이 같을 경우에는 음수 출력
                    print(-heapq.heappop(max_hq))
            else:
                print(heapq.heappop(min_hq))
        else:
            if max_hq: #둘다 비어있을 경우를 대비하는 것
                print(-heapq.heappop(max_hq))
            else:
                print(0)
