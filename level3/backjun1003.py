n = int(input())
results = []
a = 0


def fibonacci(n):
    count_zero = 0
    count_one = 0
    if n == 0:
        count_zero += 1
    elif n == 1:
        count_one += 1
    else:
        count_zero = results[n - 1][0] + results[n - 2][0]
        count_one = results[n - 1][1] + results[n - 2][1]
    return (count_zero, count_one)


for i in range(41):
    results.append(fibonacci(i))

for _ in range(n):
    test = int(input())
    print(f'{results[test][0]} {results[test][1]}')