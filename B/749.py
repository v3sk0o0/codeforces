#!/usr/local/bin/python3.4

A = set()
x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

A.add((x1, y1))
A.add((x2, y2))
A.add((x3, y3))

x, y = x1 - x2, y1 - y2

A.add((x3 + x, y3 + y))

A.add((x3 - x, y3 - y))


x, y = x2 - x3, y2 - y3

A.add((x1 + x, y1 + y))

A.add((x1 - x, y1 - y))

x, y = x1 - x3, y1 - y3

A.add((x2 + x, y2 + y))

A.add((x2 - x, y2 - y))

A.remove((x1, y1))
A.remove((x2, y2))
A.remove((x3, y3))

print(len(A))
for x, y in A:
    print(str(x) + " " + str(y))
