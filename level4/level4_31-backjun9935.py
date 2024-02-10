strings = input()
bomb = input()
last = bomb[-1]
bomb_length = len(bomb)
stack = []

for s in strings:
    stack.append(s)
    if s == last and ''.join(stack[-bomb_length:]) == bomb:
        del stack[-bomb_length:]

answer = ''.join(stack)

if answer == '':
    print("FRULA")
else:
    print(answer)