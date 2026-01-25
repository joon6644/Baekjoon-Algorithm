import sys
input = sys.stdin.readline

mod = 1_000_000_000
n = int(input())

if n == 0:
    print(0)
    print(0)
    sys.exit()
elif n < 0 and n % 2 == 0:
    print(-1)
else:
    print(1)

n = abs(n)
pre = 0
cur = 1

for i in range(2, n + 1):
    pre, cur = cur, (cur + pre) % mod

print(cur)