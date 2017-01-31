#!/usr/local/bin/python3.4
from collections import *
import pdb
usb, ps_2 , both = map(int, input().split())

sales_usb = deque() 
sales_ps_2 = deque()



for  _  in range(int(input())):
    value, type_ = input().split()
    value = int(value)
    if type_ == "USB":
        sales_usb.append(value)
    else:
        sales_ps_2.append(value)




def remove_both(usb,ps,both):
    total = 0
    sold = 0
    while both != 0:
        if (len(usb)!=0 and len(ps)!=0):
            if ( usb[0] >= ps[0] ):
                total+= ps.popleft()
                sold+=1
                both-=1
            elif ( usb[0] <  ps[0] ):
                total+= usb.popleft()
                sold+=1
                both-=1
        elif  len(usb)==0 and len(ps)!=0:
            temp_total,temp_sold,_ = remove_single(ps,both)
            total+=temp_total
            sold+=temp_sold
            both=0
        elif len(ps)==0 and len(usb)!=0:
            temp_total,temp_sold,_ = remove_single(usb,both)
            total+=temp_total
            sold+=temp_sold
            both=0
        else: 
            both=0

    
    return total,sold

def remove_single(slist,number):
    total = 0
    sold =  0
    while  number!=0  and len(slist)>0:
        total+=slist.popleft()
        sold+=1
        number-=1
    return total,sold,slist


sum_all=0
sold=0 
sales_usb = sorted(sales_usb)
sales_ps_2 = sorted(sales_ps_2)

# print (sales_usb,sales_ps_2)


t_sum_all, t_sold, sales_ps_2 = remove_single(deque(sales_ps_2),ps_2)

sum_all+=t_sum_all
sold+=t_sold


t_sum_all, t_sold, sales_usb  = remove_single(deque(sales_usb),usb)

sold+=t_sold
sum_all+=t_sum_all


t_sum_all, t_sold  = remove_both(deque(sales_usb),deque(sales_ps_2),both)

sum_all+=t_sum_all
sold+=t_sold



print (sold, sum_all)





