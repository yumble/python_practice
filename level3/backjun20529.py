# 비둘기집 원리
from itertools import combinations

t = int(input())

def mbti_distance(n, mbti):
    min_distance = 100
    if n > 32:
        return 0
    for i, j, k in combinations(mbti, 3):
        cnt = 0
        for m in range(4):
            if i[m] != j[m]:
                cnt += 1
            if j[m] != k[m]:
                cnt += 1
            if k[m] != i[m]:
                cnt += 1
        if min_distance > cnt:
            min_distance = cnt
    return min_distance



for _ in range(t):
    n = int(input())
    mbti = list(map(str, input().split()))
    print(mbti_distance(n, mbti))