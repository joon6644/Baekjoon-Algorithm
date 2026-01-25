import sys
input = sys.stdin.readline

mod = 1_000_000_000
n = int(input())

if n == 0:
    print(0)
    print(0)
    sys.exit()

pre = 0
cur = 1

if n >= 0:
    for i in range(2, n + 1):
        nxt = (cur + pre) % mod
        pre = cur
        cur = nxt
 
elif n < 0:
    n = - n
    for i in range(2, n + 1):
        nxt = pre - cur
        if nxt > 0:
            nxt %= mod
        else:
            nxt = - ((- nxt) % mod)
        pre = cur
        cur = nxt

ans = cur
print(1 if ans > 0 else -1)
print(abs(ans) % mod)