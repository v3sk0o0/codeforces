for  _ in range(int(input())):
    a, b, n, S  =  list(map(int, input().split()))
    # https://codeforces.com/problemset/problem/1256/A

    t = S % n 

    if b >= t:
        b = b - t
        S = S - t
    
        a += int(b / n)      
        b = b % n  
    
        times =  int(S /  n) 

        if  times <= a and times*n == S:
            print("YES")
        else:
            print("NO")
    
    else:
        times =  int(S /  n)

        if  times <= a and times*n == S:
            print("Yes")
        else:
            print("No")
    
