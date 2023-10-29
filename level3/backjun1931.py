n = int(input())

array = [tuple(map(int, input().split())) for _ in range(n)]

array.sort(key=lambda x: (x[1], x[0]))
conference, end = 0, 0
for conf_start, conf_end in array:
    if conf_start >= end:
        end = conf_end
        conference += 1
print(conference)
