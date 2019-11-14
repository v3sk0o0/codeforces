
q  = int(input())

while q:
    _ = input()

    A = map(int, input().split())

    value=0

    for i in sorted(A)[::-1]:
        if value >= i:
            break

        value += 1
    print(value)
    q -= 1
