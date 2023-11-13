a = int(input())
b = int(input())
button = []
if(b != 0):
    button = list(map(str, input().split()))

count = abs(100-a)


for i in range(1000001):
    for j in str(i):
        if j in button:
            break
    else: # else문 위치 중요
        count = min(count, (len(str(i)) + abs(a-i)))
print(count)
#완전탐색은 이런거구나....