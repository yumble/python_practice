n = int(input())
#
# cnt = 0
# for i in range(1, n+1):
#     if i % 10 == 5:
#         cnt += 1
#     tmp = i
#     while tmp != 0:
#         if tmp % 10 != 0:
#             break
#         cnt += 1
#         tmp //= 10
#
# print(cnt)

l = []
l.append(0)
a = 1
for i in range(1, n+1):
    a *= i
    l.append(a)
cnt = 0
i = l[n]

while i != 0:
    tmp = i
    if tmp % 10 != 0:
        break
    cnt += 1
    i //= 10
print(cnt)