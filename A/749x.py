#!/usr/local/bin/python3.4
N = int(input())


if N % 2 == 0:
    times = N / 2

else:
    times = (N - 3) / 2

result = list()
for _ in range(0, int(times)):
    result.append(2)

if N % 2 != 0:
    result.append(3)
print(len(result))
print(*result, sep=" ")
