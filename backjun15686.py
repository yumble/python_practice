import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

# city_map = []
# for _ in range(n):
#     city_map.append(list(map(int,input().split())))
#
# chicken_list = []
# home_list = []
# for i in range(n):
#     for j in range(n):
#         if city_map[i][j] == 0:
#             continue
#         elif city_map[i][j] == 1:
#             home_list.append((i,j))
#         elif city_map[i][j] == 2:
#             chicken_list.append((i,j))
# total_distance = []
# for chicken in combinations(chicken_list, m):
#     chicken_distance = []
#     for (home_i, home_j) in home_list:
#         distance_candidate_list = []
#         for (chicken_i, chicken_j) in chicken:
#             distance = abs(chicken_i-home_i) + abs(chicken_j-home_j)
#             distance_candidate_list.append(distance)
#         chicken_distance.append(min(distance_candidate_list))
#     total_distance.append(sum(chicken_distance))
#
# print(sorted(total_distance)[0])

houses = []
chickens = []
for i in range(n):
    for j, v in enumerate(map(int, input().split())):
        if v == 1:
            houses.append((i,j))
        elif v == 2:
            chickens.append((i,j))

def get_dist(house, chicken):
    return abs(house[0]-chicken[0]) + abs(house[1]-chicken[1])

ans = 2 * n * len(houses)

for combi in combinations(chickens, m):
    tot = 0 # 도시의 치킨 거리
    for house in houses:
        tot += min(get_dist(house, chicken) for chicken in combi)
    ans = min(ans, tot)

print(ans)
