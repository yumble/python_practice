n= int(input())

apprv_list = []
for _ in range(n):
    age, name = input().split()
    apprv_list.append((int(age),name))

apprv_list.sort(key=lambda x: x[0])

for apprv in apprv_list:
    print(f'{apprv[0]} {apprv[1]}')