import sys
input = sys.stdin.readline

S = int(input())
st = 2 * S 

N = 1
while True:
    if N * (N + 1) > st:
        break
    N += 1

print(N - 1)