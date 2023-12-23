from itertools import permutations

n, m = map(int, input().split())

arr = sorted(list(map(int, input().split())))

# results = set()
# for nums in permutations(arr, m):
#     results.add(nums)
results = sorted(dict.fromkeys(permutations(arr, m)))
for result in results:
    print(*result)