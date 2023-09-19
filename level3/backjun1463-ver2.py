# ver 2 DP
import sys
sys.setrecursionlimit(100000000)
def min_operations_to_one(N, memo):

    if N == 1:
        return 0

    if memo[N] != -1:
        return memo[N]

    result = 1 + min_operations_to_one(N-1, memo)
    if N % 3 == 0 :
        result = min(result, 1 + min_operations_to_one(N//3,memo))
    if N % 2 == 0 :
        result = min(result, 1 + min_operations_to_one(N//2,memo))

    memo[N] = result
    return result

N = int(input())
memo = [-1] * (N+1)
result = min_operations_to_one(N, memo)
print(result)
