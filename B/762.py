#!/usr/local/bin/python3.4
from collections import deque

usb, ps_2, both = map(int, input().split())

sales_usb = deque()
sales_ps_2 = deque()


for _ in range(int(input())):
    value, type_ = input().split()
    value = int(value)
    if type_ == "USB":
        sales_usb.append(value)
    else:
        sales_ps_2.append(value)


def remove_both(usb_, ps, both_):
    total = 0
    sold_ = 0
    while both_ != 0:
        if len(usb_) != 0 and len(ps) != 0:
            if usb_[0] >= ps[0]:
                total += ps.popleft()
                sold_ += 1
                both_ -= 1
            elif usb_[0] < ps[0]:
                total += usb_.popleft()
                sold_ += 1
                both_ -= 1
        elif len(usb_) == 0 and len(ps) != 0:
            temp_total, temp_sold, _ = remove_single(ps, both_)
            total += temp_total
            sold_ += temp_sold
            both_ = 0
        elif len(ps) == 0 and len(usb_) != 0:
            temp_total, temp_sold, _ = remove_single(usb_, both_)
            total += temp_total
            sold_ += temp_sold
            both_ = 0
        else:
            both_ = 0

    return total, sold_


def remove_single(slist, number):
    total = 0
    sold_ = 0
    while number != 0 and len(slist) > 0:
        total += slist.popleft()
        sold_ += 1
        number -= 1
    return total, sold_, slist


sum_all = 0
sold = 0
sales_usb = sorted(sales_usb)
sales_ps_2 = sorted(sales_ps_2)

# print (sales_usb,sales_ps_2)


t_sum_all, t_sold, sales_ps_2 = remove_single(deque(sales_ps_2), ps_2)

sum_all += t_sum_all
sold += t_sold


t_sum_all, t_sold, sales_usb = remove_single(deque(sales_usb), usb)

sold += t_sold
sum_all += t_sum_all


t_sum_all, t_sold = remove_both(deque(sales_usb), deque(sales_ps_2), both)

sum_all += t_sum_all
sold += t_sold


print(sold, sum_all)
