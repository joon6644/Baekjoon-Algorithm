import sys
input = sys.stdin.readline

S1 = input().rstrip()
S2 = input().rstrip()

len_S1, len_S2 = len(S1), len(S2)
dp = [[0] * (len_S1 + 1) for _ in range(len_S2 + 1)]

for r in range(1, len_S2 + 1):
    for c in range(1, len_S1 + 1):
        if S1[c - 1] == S2[r - 1]:
            dp[r][c] = dp[r - 1][c - 1] + 1
        else:
            dp[r][c] = max(dp[r - 1][c], dp[r][c - 1])

print(dp[-1][-1])