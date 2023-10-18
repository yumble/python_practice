n = int(input())

square = []
for _ in range(n):
    square.append(list(map(int, input().split())))

white, blue = 0, 0
def check(x, y, length):
    global white, blue
    color = square[y][x]

    for i in range(x, x + length):
        for j in range(y, y+length):
            if color != square[j][i]:
                check(x, y, length // 2)
                check(x + length // 2, y, length // 2)
                check(x, y + length // 2, length // 2)
                check(x + length // 2, y + length // 2, length // 2)
                return
    if color == 0:
        white += 1
    else:
        blue += 1

check(0, 0, n)
print(white)
print(blue)

