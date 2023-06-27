# 초기화
cache = [-1] * 91
cache[0] = 0
cache[1] = 1

# # old fibonacci
# def f(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return f(n-1) + f(n-2)

def f(n):
    if cache[n] == -1:
        cache[n] = f(n-1) + f(n-2)
    return cache[n]


print(f(int(input())))