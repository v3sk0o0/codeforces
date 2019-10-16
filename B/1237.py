import sys

_  = input()
before_tunel = list(map(int,sys.stdin.readline().split()))
after_tunel  = list(map(int,sys.stdin.readline().split()))


speedy_drivers = set()

while before_tunel:

    if after_tunel[-1] in speedy_drivers:
        after_tunel.pop()
        continue

    last_driver = before_tunel.pop()
    
    if after_tunel[-1] == last_driver:
        after_tunel.pop()
        continue
        
    if after_tunel[-1] in speedy_drivers:
        after_tunel.pop()
        continue

    speedy_drivers.add(last_driver)
    
print(len(speedy_drivers))

