import sys
input = sys.stdin.readline

N = int(input())

dp = [x for x in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, i):
        square = j * j
        if square > i:
            break

        if dp[i] > dp[i - square] + 1:
            dp[i] = dp[i - square] + 1

print(dp[N])