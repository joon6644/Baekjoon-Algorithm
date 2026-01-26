import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pack, each = float('inf'), float('inf')

for _ in range(M):
    p, e = map(int, input().split())
    if p < pack:
        pack = p
    if e < each:
        each = e

if pack > 6 * each:
    print(each * N)
else:
    print(min((N // 6) * pack + (N % 6) * each, ((N // 6) + 1) * pack))