_N, L, R, K = list(map(int, input().split()))

A = list(map(int, input().split()))


def solution(a_, l_, r_, k_):

    high_bound = r_
    low_bound = l_
    #    if K < L:
    #        return [-1]

    steps = [(l_, r_)]

    previous_element = None

    for i in a_[::-1]:
        if not previous_element:
            previous_element = i
            continue
        if previous_element == i:
            steps.append(steps[-1])
            continue
        if previous_element > i:
            low, high = steps[-1]
            new_high = high - 1
            new_low = max(low_bound, low - k_)

            if new_high < low_bound:
                return [-1]

            steps.append((new_low, new_high))
            previous_element = i
            continue
        if previous_element < i:
            low, high = steps[-1]
            new_low = low + 1
            new_high = min(high_bound, high + k_)
            if new_low > high_bound:
                return [-1]
            steps.append((new_low, new_high))
            previous_element = i
            continue

    steps = steps[::-1]

    d = [steps[0][0]]
    last_value = steps[0][0]
    _last_index = None
    current_value = a_[0]
    for index, value in enumerate(a_):
        if index == 0:
            current_value = a_[0]
            last_index = steps[0]
            continue

        if value == current_value:
            d.append(last_value)
            continue

        if value > current_value:

            last_value = min(max(last_value + 1, steps[index][0]), steps[index][1])

            d.append(last_value)
            current_value = value
            continue

        if value < current_value:

            last_value = min(max(steps[index][0], last_value - k_), steps[index][1])
            d.append(last_value)
            current_value = value
            continue
    return d


print(*(solution(A, L, R, K)))
