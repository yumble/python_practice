import sys

input = sys.stdin.readline

books = dict()

for _ in range(int(input())) :
    book = input()
    if book in books:
        books[book] += 1
    else:
        books[book] = 1

m = max(books.values())
candidates = []
for k, v in books.items():
    if v == m:
        candidates.append(k)
print(sorted(candidates)[0])
