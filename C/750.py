#!/usr/local/bin/python3.4


def is_possible(lst):
    flag = False
    for (_a, b) in lst:
        if b == 1:
            flag = True
        if flag and b == 2:
            return True

    return False


def find_val(lst):

    a, b = lst[0]
    for i in range(1, len(lst)):
        c, d = lst[i]
        if b == 2 and d == 1:
            return a
        a, b = c, d


def calc(N_):

    first, second = map(int, input().split())

    cont = list()

    cont.append((0, second))

    old_change = first

    current_value = 0

    last_value = first

    for _ in range(N_ - 1):

        change, division = map(int, input().split())

        current_value += old_change

        cont.append((current_value, division))

        old_change = change

        last_value = current_value + change

    # pbd.set_trace()
    #    print (last_value)
    sort_cont = sorted(cont)

    if all(division == 1 for (change, division) in sort_cont):
        return "Infinity"

    if all(division == 2 for (change, division) in sort_cont):
        change, _division = sort_cont[-1]
        #        pdb.set_trace()

        return 1899 - change + last_value

    if not is_possible(sort_cont):
        return "Impossible"

    return 1899 - find_val(sort_cont) + last_value


N = int(input())
print(calc(N))
