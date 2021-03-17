import sys
import math
# https://codeforces.com/problemset/problem/1203/C
_ = input()
A = list(map(int, sys.stdin.readline().split()))


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


def f(A_):
    min_element = min(A_)

    A_ = list(filter(lambda x: x % min_element != 0, A_))
    for i in A_:
        if gcd(min_element, i) < min_element:
            min_element = gcd(min_element, i)

        if min_element == 1:
            print(1)
            return

    if min_element == 1:
        print(1)
        return
    number_of_2 = 0
    while min_element % 2 == 0:
        # dictionary[2] = dictionary.get(2, 0) + 1
        number_of_2 += 1
        min_element /= 2

    all_divs = number_of_2 + 1

    for i in range(3, int(math.sqrt(min_element)) + 4, 2):

        cnt = 1
        if min_element < i:
            break
        while min_element % i == 0:
            #       dictionary[i] = dictionary.get(i, 0) + 1
            min_element /= i
            cnt += 1

        all_divs *= cnt

    # Something is squared
    if min_element > 2:
        all_divs *= 2

    print(all_divs)


f(A)
