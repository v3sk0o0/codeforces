from typing import Dict
n = int(input())
first_number = int(input())
second_number = int(input())

default = 0


def split_to_dict(number_: int) -> Dict:
    default_ = 0
    temp = dict()

    for number_int in map(int, str(number_)):
        temp[number_int] = temp.get(number_int, default_) + 1

    return temp


Sherlock_dict, Moriarty_dict = split_to_dict(first_number), split_to_dict(second_number)

lost = 0
left = 0
won = 0
for number in range(0, 10):
    """ Problematic!"""
    valueM = Moriarty_dict.get(number, 0)
    valueS = Sherlock_dict.get(number, 0)
    if Moriarty_dict.get(number, 0) == 0:
        left += Sherlock_dict.get(number, 0)
        continue
    elif Sherlock_dict.get(number, 0) == 0:
        lost += valueM
    elif valueM > valueS:
        won += valueS
        if left == 0:
            left += valueS
        elif valueM - valueS <= left:
            left -= valueM - valueS
        else:
            lost = (valueM - valueS) - left
            left = 0

    else:
        won += valueM
        lost = valueS - valueM

print(lost, won)
