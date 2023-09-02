import sys
input = sys.stdin.readline

n, m = map(int, input().split())

listeners = set()
for i in range(n):
    listeners.add(input())

viewers = set()
for i in range(m):
    viewers.add(input())

result = sorted(list(listeners & viewers))

print(len(result))
for person in result:
    print(person.strip())