#!/usr/bin/env python

t = int(input())

def solve(n):

    if n < 2019:
        return  "NO"
    times =  n // 2020
    return "YES" if times * 2020 <= n <= times * 2020 + times else "NO"
    
    
while t:
    
    n = int(input())

    print(solve(n))

    t -= 1
