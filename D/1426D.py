import sys
 
_n = sys.stdin.readline()
A = list(map(int, sys.stdin.readline().split()))
 
partial_sum_cache = set()
count = 0
last_sum = 0
for element in A:

    partial_sum = element + last_sum    
    last_sum = partial_sum

    if partial_sum == 0 or partial_sum in partial_sum_cache:
        count += 1
        partial_sum_cache = set()
        last_sum = element
    partial_sum_cache.add(last_sum)

 
print(count)
