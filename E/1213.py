# https://codeforces.com/contest/1213/problem/E
import sys

n = int(input())
s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()


def fifi(n_, s_, t_):

    yo = set("abc")
    prexises = ["abc", "acb", "bac", "bca", "cab", "cba"]

    if n_ == 1:
        for prexis in prexises:
            if s_ not in prexis and t_ not in prexis:
                print("YES")
                print(prexis)
                return
    else:
        for prexis in prexises:
            if s_ not in (prexis * 2) and t_ not in (prexis * 2):
                print("YES")
                print(prexis * n_)
                return

    if s_[0] == t_[0]:
        rest_element = yo - set(s_[0])
        print("YES")
        print(rest_element.pop() * n_ + rest_element.pop() * n_ + s_[0] * n_)
    elif s_[1] == t_[1]:
        rest_element = yo - set(s_[1])
        print("YES")
        print(s_[1] * n_ + rest_element.pop() * n_ + rest_element.pop() * n_)
    elif s_[1] == t_[0] and s_[0] == t_[1]:
        rest_element = yo - set(s_)
        print("YES")
        print(s_[0] * n_ + rest_element.pop() * n_ + s_[1] * n_)
    else:
        print("NO")


fifi(n, s, t)
