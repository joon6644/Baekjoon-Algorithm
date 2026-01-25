import sys
input = sys.stdin.readline

N = int(input())

prev = [1] * 10
prev[0] = 0

for _ in range(N - 1):
    curr = [0] * 10
    for i in range(10):
        if i == 0:
            curr[i] = prev[i + 1]
        elif i == 9:
            curr[i] = prev[i - 1]
        else:
            curr[i] = prev[i - 1] + prev[i + 1]
        curr[i] %= 1000000000
        
    prev = curr

print(sum(prev) % 1000000000)