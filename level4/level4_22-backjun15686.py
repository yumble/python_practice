from itertools import combinations

N, M = map(int, input().split())

houses = []
chickens = []
for i in range(N):
    for j, v in enumerate(map(int, input().split())):
        if v == 1:
            houses.append((i, j))
        elif v == 2:
            chickens.append((i, j))


def get_dist(house, chicken):
    return abs(house[0] - chicken[0]) + abs(house[1] - chicken[1])

ans = 2 * N * len(houses)

for combi in combinations(chickens, M):
    distance = 0
    for house in houses:
        distance += min(get_dist(house, chicken) for chicken in combi)
    ans = min(ans, distance)

print(ans)