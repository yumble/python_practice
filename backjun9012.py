import sys

for _ in range(int(sys.stdin.readline())):
    stk = []
    isVPS = True
    for ch in sys.stdin.readline().strip():
        if ch == '(':
            stk.append(ch)
        else:
            if stk:
                stk.pop()
            else:
                isVPS = False
                break
    if stk:
        isVPS = False
    print('YES' if isVPS else 'NO')