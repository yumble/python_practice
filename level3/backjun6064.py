n = int(input())

# x + m * a = y + n * b
# n으로 모드연산해보자
# ( x + m * a ) mod n = y
# ( x + m * a - y ) mod n = 0

for _ in range(n):
    M, N, x, y = map(int, input().split())
    for X in range(x, M*N + 1, M):
        if (X-y) % N == 0:
            print(X)
            break
    else :
        print(-1)