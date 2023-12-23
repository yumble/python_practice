from itertools import combinations_with_replacement as cwr

n, m = map(int, input().split())

arr = sorted(list(map(int, input().split())))

results = sorted(dict.fromkeys(cwr(arr, m)))
for result in results:
    print(*result)