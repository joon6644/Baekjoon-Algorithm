import sys
input = sys.stdin.readline
INF = float('inf')
h, d = INF, INF

for _ in range(3):
    h = min(h, int(input()))

for _ in range(2):
    d = min(d, int(input()))

print(h + d - 50)