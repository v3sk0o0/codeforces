
# https://codeforces.com/problemset/problem/1257/B
q = int(input())
while q:


    x, y = input().split()
    x = int(x)
    y = int(y)
    q -= 1
    if x == 1 and y >1:
        print("NO")
        continue
    if x==2 and y >3:
        print("NO")
        continue
    if x==3 and  y > 3:
        print("NO")
        continue
    print("YES")
