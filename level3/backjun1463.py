count = 0


def oper(n):
    global count
    if n == 1:
        return count
    if n % 3 == 0 and n % 2 == 0:
        min(oper(n / 3), oper(n / 2), oper(n-1))
    elif n % 3 == 0:
        min(oper(n / 3), oper(n-1))
    elif n % 2 == 0:
        min(oper(n / 2), oper(n-1))
    else:
        oper(n - 1)
    count += 1
    return count

n = int(input())
print(oper(n))
