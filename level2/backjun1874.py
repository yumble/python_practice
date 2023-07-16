import sys
input = sys.stdin.readline

n = int(input())
numbers = []
for _ in range(n):
    numbers.append(int(input()))

stack = []
print_list = []
stack_number = 1
for number in numbers:
    while stack_number <= number:
        stack.append(stack_number)
        stack_number += 1
        print_list.append("+")
    if stack.pop() != number:
        print_list = ["NO"]
        break
    print_list.append("-")
for p in print_list:
    print(p)
