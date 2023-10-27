
def solve(x, y, n, ans):

    if n == 0:
        return ans
    next = n // 2
    if x < next and y < next:
        return solve(x, y, next, ans)
    elif x >= next and y < next:
        return solve(x - next, y, next, ans + next**2)
    elif x < next and y >= next:
        return solve(x, y - next, next, ans + (next**2)*2)
    else:
        return solve(x - next, y - next, next, ans + (next**2) * 3)

N, r, c = map(int, input().split())
print(solve(c, r, 2**N, 0))