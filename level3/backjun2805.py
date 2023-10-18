n, m = map(int, input().split())
trees = list(map(int, input().split()))

low = 0
high = max(trees)
mid = (low+high) // 2
ans = 0

def is_possible():
    global mid, trees
    return sum( tree-mid for tree in trees if tree > mid) >= m
while low <= high:
    if is_possible():
        low = mid + 1
        ans = mid
    else:
        high = mid - 1
    mid = (low+high) // 2
print(ans)