M = 1234567891
r = 31

n = int(input())
hash_str = input()

result = 0
for i in range(len(hash_str)):
    tmp = ord(hash_str[i]) - 96
    tmp *= r ** i
    result += tmp

print(result % M)