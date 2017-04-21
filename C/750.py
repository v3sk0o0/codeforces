#!/usr/local/bin/python3.4

import pdb


def ispossible(lst):
    flag = False
    for (a, b) in lst:
        if b == 1:
            flag = True
        if flag and b == 2:
            return True

    return False


def findval(lst):

    a, b = lst[0]
    for i in range(1, len(lst)):
        c, d = lst[i]
        if b == 2 and d == 1:
            return a 
        a, b = c, d


def calc(N):
    
    curent_value = 0

    first, second = map(int, input().split())

    cont = list()
    
    cont.append((0, second))
    
    old_change = first
    
    current_value = 0 
    
    last_value = first
   
    for _ in range(N - 1):
    
        change, division = map(int, input().split())
    
        current_value += old_change
    
        cont.append((current_value, division))

        old_change = change

        last_value = current_value + change
    

# pbd.set_trace()
#    print (last_value)   
    sort_cont = (sorted(cont))  
    
    if all(division == 1 for (change, division) in sort_cont):
        return "Infinity"
    
    if all(division == 2 for (change, division) in sort_cont):
        change, divsion = sort_cont[-1]
#        pdb.set_trace()
 
        return 1899 - change + last_value

    if not ispossible(sort_cont):
        return "Impossible"
   
    return 1899 - findval(sort_cont) + last_value


N = int(input())
print(calc(N))
