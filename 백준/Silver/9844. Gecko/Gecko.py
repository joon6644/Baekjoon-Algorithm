import sys
input = sys.stdin.readline

h, w = map(int, input().split())

dp = [0] * w

for _ in range(h):
    line = list(map(int, input().split()))
    
    next_dp = [0] * w
    
    for i in range(w):
        if w == 1:
            next_dp[i] = line[i] + dp[i]
            
        elif i == 0:
            next_dp[i] = line[i] + max(dp[i], dp[i + 1])
            
        elif i == w - 1:
            next_dp[i] = line[i] + max(dp[i - 1], dp[i])
            
        else:
            next_dp[i] = line[i] + max(dp[i - 1], dp[i], dp[i + 1])
            
    dp = next_dp

print(max(dp))