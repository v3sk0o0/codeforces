from itertools import combinations
from typing import Tuple
from math import ceil, sqrt


def is_prime(a):
    """ Modified a"""
    if a == 1:
        return False
    if a == 2:
        return True
    return all(a % i for i in range(2, ceil(sqrt(a) + 1)))


def convert_to_decimal_int(values: Tuple[int]) -> int:

    decimal_int: int = 0
    for number in values:
        decimal_int *= 10
        decimal_int += int(number)
    return decimal_int


def solve(number: str) -> int:

    for combination_size in range(1, len(number)):

        for next_number in combinations(number, combination_size):

            decimal_int = convert_to_decimal_int(next_number)
            if not is_prime(decimal_int):
                return decimal_int

    return int(number)


if __name__ == "__main__":

    number_of_times = int(input())

    while number_of_times:

        _n = input()

        number = str(input())

        limited_number = solve(number)

        print(len(str(limited_number)))
        print(limited_number)

        number_of_times -= 1
