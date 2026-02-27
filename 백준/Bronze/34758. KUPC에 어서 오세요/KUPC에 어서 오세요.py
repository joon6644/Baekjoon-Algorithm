import sys
input = sys.stdin.readline

X, Y = map(int, input().split())
N = int(input())
for _ in range(N):
    x, y = map(int, input().split())

    if x == X or y == Y:
        sys.stdout.write("0\n")
    else:
        sys.stdout.write("1\n")