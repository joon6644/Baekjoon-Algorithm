import sys
input = sys.stdin.readline

n = int(input())

array = [0]
for _ in range(n):
    array.append(int(input()))

if n < 3:
    print(sum(array))
    sys.exit()

dp = [0] * (n + 1)
dp[1] = array[1]
dp[2] = array[1] + array[2]

for i in range(3, n + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + array[i], dp[i - 3] + array[i - 1] + array[i])

print(dp[-1])