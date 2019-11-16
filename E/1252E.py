

_N, L, R, K  =  list(map(int, input().split()))

A = list(map(int, input().split()))


def solution(A, L, R, K):

    HIGH_BOUND = R
    LOW_BOUND = L
#    if K < L:
#        return [-1]

    steps = [(L,R)]

    previous_element = None

    for i in A[::-1]:
        if not previous_element:
            previous_element = i
            continue
        if previous_element == i:
            steps.append(steps[-1])
            continue
        if previous_element > i:
            low, high  = steps[-1]
            new_high = high - 1
            new_low = max(LOW_BOUND, low - K)

            if new_high < LOW_BOUND:
                return [-1]

            steps.append((new_low, new_high))
            previous_element = i
            continue
        if previous_element < i:
            low, high = steps[-1]
            new_low = low +1
            new_high = min(HIGH_BOUND, high + K)
            if new_low > HIGH_BOUND:
                return [-1]
            steps.append((new_low, new_high))
            previous_element = i
            continue


    steps = steps[::-1]

    D = [steps[0][0]]
    last_value = steps[0][0]
    last_index = None
    for index, value in enumerate(A):
        if index == 0:
            current_value = A[0]
            last_index = steps[0]
            continue

        if value == current_value:
            D.append(last_value)
            continue

        if value > current_value:

            last_value = min(max(last_value+ 1, steps[index][0]), steps[index][1])

            D.append(last_value)
            current_value = value
            continue

        if value < current_value:

            last_value = min(max(steps[index][0], last_value - K), steps[index][1])
            D.append(last_value)
            current_value = value
            continue
    return D

print(*(solution(A,L,R, K)))
