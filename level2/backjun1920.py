from bisect import bisect_left, bisect_right

n = int(input())
num_list = list(map(int, input().split()))
num_list.sort()
m = int(input())
check_list = list(map(int,input().split()))

for check in check_list:
    boolean = bisect_right(num_list, check) - bisect_left(num_list, check)
    if boolean:
        print("1")
    else:
        print("0")