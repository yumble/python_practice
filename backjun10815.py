from bisect import bisect_left, bisect_right
import sys

input = sys.stdin.readline

n = int(input())
cards = sorted(list(map(int,input().split()))) #!!!!!
m = int(input())
compares = list(map(int,input().split()))
ans = []

for c in compares:
    l = bisect_left(cards, c)
    r = bisect_right(cards, c) # or  if cards[l] == c : 이면 존재.
    ans.append(1 if r -l else 0) #!!!!

print(*ans)
#print(' '.join(map(str, ans)))