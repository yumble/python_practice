import sys

def custom_round(val):
    return int(val) + 1 if val - int(val) >= 0.5 else int(val)
def lev(n):
    if not n:
        return 0
    levels = [int(input()) for _ in range(n)]

    levels.sort()

    cut = custom_round(n * 0.15)

    levels = levels[cut:len(levels) - cut]

    avr = sum(levels) / len(levels)

    return custom_round(avr)

input = sys.stdin.readline

n = int(input())

print(lev(n))
