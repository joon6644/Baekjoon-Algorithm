import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
K = int(input())

max_limit = max(arr) * K + 2
dp = [float('inf')] * max_limit
dp[0] = 0

ans = 0
for i in range(1, max_limit):
    for num in arr:
        if i >= num:
            dp[i] = min(dp[i], dp[i - num] + 1)

    if dp[i] > K:
        ans = i
        break

if ans % 2 == 0:
    print(f"holsoon win at {ans}")
else:
    print(f"jjaksoon win at {ans}")