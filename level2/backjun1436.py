# n = int(input())
#
# cnt = 0
# ans = 0
# while cnt != n:
#     ans += 1
#     tmp = ans
#     while tmp != 0:
#         if tmp % 1000 == 666:
#             cnt += 1
#             break
#         else:
#             tmp //= 10
#
#
# print(ans)
n = int(input())
cnt = 0
result = 666

while True:
    if '666' in str(result):
        cnt += 1

    if cnt == n:
        break

    result += 1

print(result)