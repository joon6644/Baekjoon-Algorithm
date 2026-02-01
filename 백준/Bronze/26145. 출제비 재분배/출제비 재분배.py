import sys
input = sys.stdin.readline

N, M = map(int, input().split())
S = list(map(int, input().split()))
S += [0] * M

for i in range(N):
    T = map(int, input().split())
    for idx, val in enumerate(T):
        S[i] -= val
        S[idx] += val

print(*S)
