#!/usr/local/bin/python3.4
N = int(input())


if N % 2 == 0:
    times = N / 2
    print(int(times))
    print("2 " * int(times))
else:
    times = (N - 3) / 2
    print(int(times) + 1)
    print("2 " * int(times) + "3 ")
