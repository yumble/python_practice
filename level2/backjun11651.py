import sys

input = sys.stdin.readline

n = int(input())

data_list = [(a, b) for a, b in [map(int, input().split()) for _ in range(n)]]

data_list = sorted(data_list, key=lambda x:(x[1], x[0]))

for data in data_list:
    print(f'{data[0]} {data[1]}')