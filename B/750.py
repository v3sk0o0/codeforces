#!/usr/local/bin/python3.4


N = int(input())


def poles(N_):

    south = 0
    north = 1
    east = 2
    west = 3
    north_pole = 0
    south_pole = 20000
    directions = ["South", "North", "East", "West"]

    position = 0
    for _ in range(N_):

        steps, direction = input().split()
        steps = int(steps)

        if direction in (directions[east],  direction == directions[west]):
            if position in (north_pole, south_pole):
                return "NO"
        if direction == directions[south]:
            if steps + position > south_pole:
                return "NO"
            position += steps
        if direction == directions[north]:
            if position - steps < north_pole:
                return "NO"
            position -= steps

    if position == north_pole:
        return "YES"
    return "NO"


print(poles(N))
