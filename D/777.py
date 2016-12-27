#http://codeforces.com/problemset/problem/735/D
from math import *

def is_prime(a):
    if (2==a):
        return True
    else:
        return all(a % i for i in range(2, ceil(sqrt(a)+1)))


number=int(input())

def find_minimal_tax(number):

    if ( number == 2 or is_prime(number)):
        return 1
    for i in range(2,number):
        if number % i == 0 and is_prime(i):
           return i
    
    

print (find_minimal_tax(number))

    
