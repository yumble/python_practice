n = int(input())
results = [0] * 101
for i in range(1, 101):
    if i <= 3:
        results[i] = 1
    elif i == 4 or i == 5:
        results[i] = 2
    else:
        results[i] = results[i-1] + results[i-5]
for _ in range(n):
    print(results[int(input())])