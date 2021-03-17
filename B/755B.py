n, m = map(int, input().split())


def is_equal(n_value: int, m_value: int) -> str:
    if n_value > m_value:
        return "YES"
    if n_value < m_value:
        return "NO"
    return "NOPE"


enemyball_words = set()
powerball_words = set()
for _ in range(n):
    powerball_words.add(input().strip())

for _ in range(m):
    enemyball_words.add(input().strip())


common_words = [word for word in enemyball_words if word in powerball_words]

if is_equal(n, m) != "NOPE":
    print(is_equal(n, m))
elif len(common_words) % 2 == 0:
    print("NO")
else:
    print("YES")
