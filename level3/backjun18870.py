n = int(input())
numbers = list(map(int, input().split()))
sort_numbers = sorted(list(set(numbers)))

dic = {sort_numbers[i] : i for i in range(len(sort_numbers))}

for num in numbers:
    print(dic[num], end=' ')
# print_list = []
# for num in numbers:
#     print_list.append(sort_numbers.index(num)) # 시간 초과 O(n^2)
# print(' '.join(map(str,print_list)))