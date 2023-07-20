test = int(input())
house = [[ 0 for _ in range(15)] for _ in range(15)]
house[0] = [i for i in range(15)]

for i in range(1,15):
    for j in range(1,15):
        house[j][i] = sum(house[j-1][:i+1])

for _ in range(test):
    n = int(input())
    m = int(input())
    print(house[n][m])