import sys

input=sys.stdin.readline

n, m, b = map(int, input().split())
mine=[list(map(int, input().split())) for _ in range(n)]

time_list = []

def craft(i):
    time = 0
    inventory = b
    for j in range(n):
        for k in range(m):
            if mine[j][k] > i:
                inventory += mine[j][k] - i
                time += 2 * (mine[j][k] - i)
            else:
                inventory -= i - mine[j][k]
                time += i - mine[j][k]

    if inventory >= 0:
        time_list.append((time, i))

for i in range(257):
    craft(i)
time_list.sort(key=lambda k:(k[0],-k[1]))
print(f'{time_list[0][0]} {time_list[0][1]}')