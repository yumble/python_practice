n = int(input())
bitonic = list(map(int, input().split()))

dp1 = [1] * n
dp2 = [1] * n

for i in range(n):
    for j in range(i):
        if bitonic[i] > bitonic[j]:
            dp1[i] = max(dp1[i], dp1[j] + 1)

bitonic.reverse()

for i in range(n):
    for j in range(i):
        if bitonic[i] > bitonic[j]:
            dp2[i] = max(dp2[i], dp2[j] + 1)
dp2.reverse()

results = []
for i in range(n):
    results.append(dp1[i] + dp2[i] - 1)

print(max(results))
