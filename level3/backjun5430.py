# import ast
from collections import deque

t = int(input())

def AC(p, input_list):
    is_forward_direction = True
    for func in p:
        if func == 'R':
            is_forward_direction = False if is_forward_direction else True
        elif func == 'D':
            if not len(input_list):
                return "error"
            if is_forward_direction:
                input_list.popleft()
            else:
                input_list.pop()
    if not is_forward_direction:
        input_list.reverse()
    return "[" + ",".join(map(str, input_list)) + "]"
for _ in range(t):
    p = input()
    n = int(input())
    input_list = input()
    if n == 0:
        input_list = []
    else:
        input_list = deque(list(map(int, input_list.strip()[1:-1].split(','))))

    print(AC(p, input_list))

