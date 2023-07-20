n = int(input())

boolean = False
for i in range(n):
    sum_num = i
    # for j in range(len(str(i))):
    #     sum += int(str(i)[j])
    sum_num += sum(map(int, str(i)))
    if sum_num == n:
        print(i)
        boolean = True
        break
if not boolean:
    print(0)