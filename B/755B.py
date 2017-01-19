
n, m = map(int , input().split())

def isEqual(n,m):
    if n > m:
        return "YES"
    if n < m:
        return "NO"
    if n == m:
        return "NOPE"

enemyball_words=set()
powerball_words=set()
for _ in range(n):
    powerball_words.add(input().strip())

for _ in range(m):
    enemyball_words.add(input().strip())


common_words = [ word for word in enemyball_words if word in powerball_words ]

if "NOPE" != isEqual(n,m):
    print ( isEqual(n,m) )
elif  len(common_words) % 2 == 0:
    print ("NO")
else:
    print ("YES")
    


