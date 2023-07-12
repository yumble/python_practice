import sys
input = sys.stdin.readline

n = int(input())
c = dict()
words = [[] for _ in range(51)]
for _ in range(n):
    word = input().rstrip('\n')
    if word not in c:
        c[word] = len(word)
for key in sorted(c, key=lambda k: (c[k], k)):
    print(key)