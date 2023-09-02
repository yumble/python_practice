import sys

input = sys.stdin.readline

n = int(input())
s = set()

for _ in range(n):
    oper = input().split()
    if oper[0] == 'add':
        s.add(int(oper[1]))
    elif oper[0] == 'remove':
        s.discard(int(oper[1]))
    elif oper[0] == 'check':
        print(1 if int(oper[1]) in s else 0)
    elif oper[0] == 'toggle':
        if int(oper[1]) in s:
            s.discard(int(oper[1]))
        else:
            s.add(int(oper[1]))
    elif oper[0] == 'all':
        s = set([i for i in range(1,21)])
    else:
        s = set()