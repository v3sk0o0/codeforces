#!/usr/bin/env python3
import operator


def partion_check(B) -> bool:
    location =0
    row = 1
    current_row = None
    active_block = None
    for index, block in enumerate(B):

        if not active_block:
            active_block = block
            continue
        if active_block:

            if  active_block[row] + 1 == block:
                return False

            if active_block[location] == block[location]:
                if (block[row] - active_block[row]) % 2 != 1:
                    return False

            else:
                if (block[row] - active_block[row])  % 2 != 0:
                    return False
            active_block = None
    return not active_block

def solve(A) -> bool:
    A.sort(key=operator.itemgetter(1))
    B = []
    for block in A:
        if not B:
            B.append(block)
            continue
        last_block = B[-1]
        if last_block[1] == block[1]:
            B.pop()
            if not partion_check(B):
                return False
            B = []
            continue
        B.append(block)
    return partion_check(B)

t = int(input())
 
while t:
    empty_line = input()   
    _m, n  = map(int, input().split())
    all_blocks = []
    while n:

        all_blocks.append(tuple(map(int, input().split())))
        n -=1
    print ("YES") if solve(all_blocks) else print("NO")

    
    t -= 1
