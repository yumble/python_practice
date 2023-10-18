parts = input().split('-')
sum = 0
for part in parts[0].split('+'):
    sum += int(part)
for part in parts[1:]:
    for j in part.split('+'):
        sum -= int(j)

print(sum)