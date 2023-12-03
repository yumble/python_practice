import heapq
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    isVisited = dict()
    for i in range(1, k+1):
        oper, number = map(str, input().split())
        number = int(number)
        if oper == 'I':
            heapq.heappush(min_heap, (number, i))
            heapq.heappush(max_heap, (-number, i))
        else:
            if not min_heap or not max_heap:
                continue
            if number == 1:
                n, count = heapq.heappop(max_heap)
                while max_heap and isVisited.get((-n, count)):
                    n, count = heapq.heappop(max_heap)
                isVisited[(-n, count)] = 1
            elif number == -1:
                n, count = heapq.heappop(min_heap)
                while min_heap and isVisited.get((n, count)):
                    n, count = heapq.heappop(min_heap)
                isVisited[(n, count)] = 1

    while max_heap:
        if not isVisited.get((-max_heap[0][0], max_heap[0][1])):
            break
        heapq.heappop(max_heap)
    while min_heap:
        if not isVisited.get((min_heap[0][0], min_heap[0][1])):
            break
        heapq.heappop(min_heap)

    if not max_heap:
        print("EMPTY")
    elif not min_heap:
        print("EMPTY")
    else:
        print(f'{-max_heap[0][0]} {min_heap[0][0]}')
