from math import sqrt, ceil

# https://codeforces.com/contest/1242/problem/A


def is_prime(a):
    if a == 1:
        return False
    if a == 2:
        return True
    return all(a % i for i in range(2, int(ceil(sqrt(a) + 1))))


n = int(input())

if n == 1:
    print(1)
elif is_prime(n):
    print(n)
else:
    numero = n
    for i in range(2, int(ceil(sqrt(n) + 3))):
        if numero % i == 0:
            while True:
                if numero % i != 0:
                    break
                numero /= i

            if numero == 1:
                print(i)
            else:
                print(1)
            break
