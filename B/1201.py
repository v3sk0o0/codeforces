#  https://codeforces.com/problemset/problem/1201/B
import sys


def f1():
    _ = input()
    A = list(map(int, sys.stdin.readline().split()))
    total_sum = sum(A)
    if sum(A) % 2 == 1:
        print("NO")
        return
    mid_val = total_sum / 2
    flag = "YES"
    for i in A:
        if i > mid_val:
            flag = "NO"

    print(flag)


f1()
