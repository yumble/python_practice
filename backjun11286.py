import heapq as hq
import sys

pq = []
input = sys.stdin.readline

for _ in range(int(input())):
    x = int(input())
    if x:
        hq.heappush(pq, (abs(x),x))
    else:
        print(hq.heappop(pq)[1] if pq else 0)


# # 2번째 방법
# import heapq as hq
# import sys
# min_heap = [] #양수
# max_heap = [] #음수 -> 최대 힙을 쓰려면 넣기전에 부호붙이고, 뺄때 부호 붙이는..
# input = sys.stdin.readline
#
# for _ in range(int(input())):
#     x = int(input())
#     if x:
#         if x > 0:
#             hq.heappush(min_heap, x)
#         else:
#             hq.heappush(max_heap, -x)
#     else:
#         # 각 힙이 먼저 비어있는지 체크
#         # 이후에 두 배열의 [0]번째 원소의 절댓값을 비교 후 출력 로직
#         if min_heap:
#             if max_heap:
#                 if min_heap[0] < abs(-max_heap[0]):
#                     print(hq.heappop(min_heap))
#                 else:
#                     print(-hq.heappop(max_heap))
#             else:
#                 print(hq.heappop(min_heap)) #max_heap이 비어있는 경우
#         else:
#             if max_heap:
#                 print(-hq.heappop(max_heap))  # min_heap이 비어있는 경우
#             else: #둘다 비어있는 경우
#                 print(0)
