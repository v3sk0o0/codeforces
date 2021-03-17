import sys

# https://codeforces.com/problemset/problem/1214/C
n = int(input())
s = input().strip()

if n % 2 == 1:
    print("No")
    sys.exit()

sum_bracket = 0

for i in s:
    if i == ")":
        sum_bracket -= 1
    if i == "(":
        sum_bracket += 1
    if sum_bracket < -1:
        print("No")
        sys.exit(0)

if sum_bracket == 0:
    print("Yes")
else:
    print("No")
