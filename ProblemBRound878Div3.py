from math import log2 

num = int(input())

for i in range(num):
    x, y = map(int, input().split())

    if log2(x) < y:
        result = x + 1
    else:
        result = int(2 ** y)

    print(result)
