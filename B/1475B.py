#!/usr/bin/env python

t = int(input())


def solve(number: int) -> str:

    if number < 2019:
        return "NO"
    times = number // 2020
    return "YES" if times * 2020 <= number <= times * 2020 + times else "NO"


while t:

    n = int(input())

    print(solve(n))

    t -= 1
