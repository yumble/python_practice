import sys

input = sys.stdin.readline

while True:
    num = input().rstrip('\n')
    if num == '0':
        break
    if len(num) == 1:
        print('yes')
        continue
    if num[:(len(num) // 2)] == ''.join(reversed(num[-(len(num) // 2):])):
        print('yes')
    else:
        print('no')
