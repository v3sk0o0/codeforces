#!/usr/bin/env python3

t = int(input())


def solve(A_) -> str:

    revese_A = sorted(A_, reverse=True)

    alice_sum = sum([value for value in revese_A[::2] if value % 2 == 0])
    bob_sum = sum([value for value in revese_A[1::2] if value % 2 != 0])

    if alice_sum == bob_sum:
        return "Tie"
    if alice_sum > bob_sum:
        return "Alice"
    return "Bob"


while t:

    _n = int(input())
    A = list(map(int, input().split()))

    print(solve(A))
    t -= 1
