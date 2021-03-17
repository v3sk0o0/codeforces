#!/usr/local/bin/python3.4

from math import ceil, sqrt


def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return a


def is_prime(a):
    if a == 2:
        return True
    return all(a % i for i in range(2, ceil(sqrt(a) + 1)))


input()
numbers = list(map(int, input().split()))

max_size = 0
for x in range(2, max(numbers)):
    current_size = 0
    if not is_prime(x):
        continue

    for y in numbers:
        if x <= y and y % x == 0:
            current_size += 1

    max_size = max(max_size, current_size)


print(max_size)
