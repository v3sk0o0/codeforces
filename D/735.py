# http://codeforces.com/problemset/problem/735/D
from math import ceil, sqrt


def is_prime(a):
    if a == 2:
        return True
    return all(a % i for i in range(2, ceil(sqrt(a) + 1)))


number = int(input())


def find_minimal_tax(number_):

    if number_ == 2 or is_prime(number_):
        return 1

    if number_ % 2 == 0 or is_prime(number_ - 2):
        return 2

    return 3


print(find_minimal_tax(number))
