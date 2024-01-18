def union(x, y):
    root_x, root_y = find(x), find(y)
    root[max(root_x, root_y)] = min(root_x, root_y)
def find(x):
    if root[x] == x:
        return x
    root[x] = find(root[x])
    return root[x]

def check(x, y):
    return find(x) == find(y)



N, M = map(int, input().split())
T, *TP = map(int, input().split())
truth = [True if i in TP else False for i in range(N+1)]
root = [i for i in range(N + 1)]
parties = []

for _ in range(M):
    number, *attendances = map(int, input().split())
    parties.append(attendances)
    for i in range(number - 1):
        union(attendances[i], attendances[i+1])

for i in range(1, N+1):
    if truth[i]:
        truth[find(i)] = True

ans = 0
for party in parties:
    for attendance in party:
        if not truth[find(attendance)]:
            ans += 1
            break
print(ans)