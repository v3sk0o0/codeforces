# https://codeforces.com/problemset/problem/1204/B
import sys

# n, l, r = input()

n, l, r = list(map(int, sys.stdin.readline().split()))
min_sum = 0
max_sum = 0
for val in range(l):
    min_sum += pow(2, val)

min_sum += n - l
max_sum = 0
for val in range(r):
    max_sum += pow(2, val)
max_sum += pow(2, (r - 1)) * (n - r)
print(min_sum, max_sum)
