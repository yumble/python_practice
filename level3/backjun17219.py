import sys
input = sys.stdin.readline

n, m = map(int, input().split())

data_list = dict()

for _ in range(n):
    site, password = map(str, input().split())
    data_list[site] = password

for _ in range(m):
    print(data_list.get(input().strip()))