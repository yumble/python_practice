import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data_list_num = dict()
data_list_pok = dict()
for i in range(1, n+1):
    poketmon = input().strip()
    data_list_num[i] = poketmon
    data_list_pok[poketmon] = i


for _ in range(m):
    tmp = input().strip()
    if tmp.isdigit():
        print(data_list_num.get(int(tmp)))
    else:
        print(data_list_pok.get(tmp))