import math

# https://codeforces.com/problemset/problem/1062/B


def B1062(n):
    initial_value = n
    dictionary = dict()
    if n == 1:
        print(n, 0)
        return
    value = 1
    while n % 2 == 0:
        dictionary[2] = 1 + dictionary.get(2, 0)
        n = n / 2
        value = 2

    for prime in range(3, int(math.sqrt(n)) + 1, 2):
        found_prime = False
        while n % prime == 0:
            dictionary[prime] = dictionary.get(prime, 0) + 1
            n = n / prime
            if not found_prime:
                value *= prime
                found_prime = True

    if n > 2:
        dictionary[n] = dictionary.get(n, 0) + 1
        value *= n

    steps = 0
    max_power = max(dictionary.values())
    math_log = math.log(max_power, 2)

    if max_power == 1:

        print(initial_value, 0)
        return

    if all(x == max_power for x in dictionary.values()) and math.log(
        max_power, 2
    ) == int(math.log(max_power, 2)):
        steps = int(math_log)
    else:
        if int(math_log) == math_log:  # max power is squared
            # we add one for the "squaredfication"
            steps = int(math_log) + 1
        else:
            steps = int(math_log) + 1 + 1

    # print(value, steps)
    print(" ".join([str(int(value)), str(steps)]))


B1062(int(input()))
