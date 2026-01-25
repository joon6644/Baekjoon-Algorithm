import sys
input = sys.stdin.readline

N = 250
dp = [1] * (N + 1)

for i in range(2, N + 1):
    dp[i] = dp[i - 1] + 2 * dp[i - 2]

while True:
    n = input().rstrip()
    if not n: break

    n = int(n)
    sys.stdout.write(str(dp[n]) + "\n")