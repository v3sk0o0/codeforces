import sys

times = int(input())

while times:
    total = 0
    _ = input()
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))

    minA = min(A)
    minB = min(B)

    for a, b in zip(A, B):

        diffA = a - minA
        diffB = b - minB

        minimal_element = min(diffA, diffB)

        total += minimal_element
        total += diffA + diffB - 2 * minimal_element

    print(total)

    total = 0
    times -= 1
