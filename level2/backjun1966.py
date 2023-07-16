import sys
from collections import deque
input = sys.stdin.readline

test = int(input())

def print_queue():
    n, m = map(int, input().split())
    priorities = list(map(int, input().split()))
    print_number = priorities[m]
    index_list = deque((index, element) for (index,element) in enumerate(priorities))
    priorities.sort(reverse=True)
    count = 1
    while True:
        now = priorities[0]
        if now == index_list[0][1]:
            if print_number == index_list[0][1] and m == index_list[0][0]:
                return count
            else:
                priorities.pop(0)
                index_list.popleft()
                count += 1
        else:
            index_list.append(index_list.popleft())

for _ in range(test):
    print(print_queue())