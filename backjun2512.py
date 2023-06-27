import sys

input = sys.stdin.readline

n = int(input())
budgets = list(map(int, input().split()))
total_budget = int(input())

# 탐색범위 설정
low = 0
high = max(budgets)
mid = (low+high) // 2
ans = 0

def is_possible(mid):
    return sum(min(budget, mid) for budget in budgets) <= total_budget

while low <= high:
    if is_possible(mid):
        low = mid + 1
        ans = mid
    else:
        high = mid - 1
    mid = (low + high) // 2

print(ans)