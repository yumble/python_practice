n = int(input())
numbers = list(map(int, input().split()))
d = dict()
for number in numbers:
    if number in d:
        d[number] += 1
    else:
        d[number] = 1

m = int(input())
check_nums = list(map(int, input().split()))
ans = []
for chk in check_nums:
    ans.append(d.get(chk, 0))
print(*ans)