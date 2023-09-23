n = int(input())
for _ in range(n):
    d = dict()
    m = int(input())
    result = 1
    for _ in range(m):
        name, dress = map(str, input().split())
        if dress in d.keys():
            d[dress] = d[dress] + 1
        else:
            d[dress] = 1

    for k, v in d.items():
        result *= v + 1
    print(result - 1)