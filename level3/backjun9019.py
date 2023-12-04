from collections import deque

T = int(input())
def D(position):
    new_position = position * 2
    new_position %= 10000
    return new_position

def S(position):
    new_position = position - 1
    new_position %= 10000
    return new_position

def L(position):
    front = position % 1000
    back = position // 1000
    return front*10 + back


def R(position):
    front = position % 10
    back = position // 10
    return front * 1000 + back


def DSLR(A, B):
    isVisited = [False] * 10000
    dq = deque()
    dq.append((A, ''))
    isVisited[A] = True

    while dq:
        position, operators = dq.popleft()
        if position == B:
            return operators

        for i in 'DSLR':
            if i == 'D':
                new_position = D(position)
                oper = 'D'
            elif i == 'S':
                new_position = S(position)
                oper = 'S'
            elif i == 'L':
                new_position = L(position)
                oper = 'L'
            elif i == 'R':
                new_position = R(position)
                oper = 'R'

            if isVisited[new_position] == False:
                new_operators = operators + oper
                dq.append((new_position, new_operators))
                isVisited[new_position] = True



for _ in range(T):
    A, B = map(int, input().split())
    print(DSLR(A, B))

