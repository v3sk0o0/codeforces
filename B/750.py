#!/usr/local/bin/python3.4
import pdb
N = int(input())

def poles(N):

    South=0
    North=1
    East=2
    West=3
    NorthPole=0
    SouthPole=20000
    directions = [ "South" , "North" , "East" , "West" ]

    position = 0
    for _ in range(N):
        
        steps, direction =  input().split()   
        steps = int(steps)
        
        if ( direction ==  directions[East] or direction == directions[West]):
            if (position != NorthPole and position != SouthPole):
                continue
            else:
                return "NO" 
        if direction == directions[South]:
            if ( steps +  position > SouthPole):
                return "NO"
            else:
                position+=steps
        if direction == directions[North]:
            if ( position - steps < NorthPole):
                return "NO"
            else:
                position-=steps
   

    if position==NorthPole:
        return "YES"
    else:
        return "NO"

print(poles(N))
