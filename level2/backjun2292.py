n = int(input())

a = 1
b = 6
count = 1
while True:
    if a >= n:
        print(count)
        break
    count += 1
    a += b
    b = 6 * count
