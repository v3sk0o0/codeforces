from collections import deque
# 5 5 5
# uuuuuyyyyybbbbbqqqqqkkkkk
 
# https://codeforces.com/contest/1267/problem/L
# quick and dirty solution -
 
n, l, k  =  list(map(int, input().split()))
 
ww = deque(sorted(input()))
 
words = deque()
 
prefix_words = deque()

while k:

    if not ww:
        break
 
    if words and len(words[0]) == l:
        prefix_words.append(words.popleft())
        k-=1
        continue
 
    if not words:
        for _ in range(0,k):
            words.append(ww.popleft())
    else:
        for _ in range(0,k):
            new_word = words.popleft()
            words.append(new_word + ww.popleft())
    
    while words:
    
        if len(words) == 1: 
            new_word = words.popleft()
            while len(new_word) != l:
                 new_word += ww.popleft()
            prefix_words.append(new_word)
            k -= 1
            break

        if words[0] == words[-1]:
            break
 
        
        new_word = words.popleft()
        prefix_words.append(new_word)
        k -= 1

for word in words:
    prefix_words.append(word)

while prefix_words:
    new_word = prefix_words.popleft()
    while len(new_word) != l:
        new_word += ww.popleft()
    print(new_word)
        
ww = list(ww)
for i in range(0, len(ww), l):
    print("".join(ww[i:i + l ]))
