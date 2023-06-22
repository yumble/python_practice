import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
coins.reverse()

coinCount =0

for coin in coins:
    if coin > k:
        continue
    if k == 0:
        break
    coinCount += k // coin
    k %= coin

print(coinCount)
#print(f'coin: {coin}, K: {K}, ans: {ans}')