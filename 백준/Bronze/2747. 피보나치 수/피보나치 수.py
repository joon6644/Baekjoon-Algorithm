import sys

n = int(sys.stdin.readline())

dp = [0] * (n + 2)
dp[1] = 0
dp[2] = 1

for i in range(3, n + 2):
    dp[i] = dp[i - 2] + dp[i - 1]

print(dp[-1])