# https://codeforces.com/contest/1213/problem/E
import sys
n = int(input())
s = sys.stdin.readline().strip()
t = sys.stdin.readline().strip()

def fifi(n, s,t):

    yo = set("abc")
    prexises = ["abc" , "acb", "bac", "bca", "cab", "cba"]
    
    
    if n == 1:
        for prexis in prexises:
            if (s not in prexis and t not in prexis):
                print("YES")
                print(prexis)
                return
    else:
        for prexis in prexises:
            if ((s not in (prexis * 2)) and (t not in (prexis * 2))):
                print("YES")
                print(prexis * n)
                return

    if s[0] == t[0]:
        rest_element = yo - set(s[0])
        print("YES")
        print( rest_element.pop() * n  + rest_element.pop() * n + s[0] *n)
        return
    elif  s[1] == t[1]:
        rest_element = yo - set(s[1])
        print ("YES")
        print(s[1] *n  + rest_element.pop() * n + rest_element.pop() *n) 
        return
    elif  s[1] == t[0] and s[0] == t[1]:
        rest_element = yo - set(s)
        print("YES")
        print(s[0] * n + rest_element.pop() * n + s[1] *  n)
    else:
        print("NO") 
        return
   
fifi(n,s,t)

