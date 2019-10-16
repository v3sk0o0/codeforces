b = int(input())
g = int(input())
n = int(input())

# https://codeforces.com/problemset/problem/1214/B

if b + g == n:
    print(1)
else:
    print( min(b,g,n, b+g - n) + 1)

