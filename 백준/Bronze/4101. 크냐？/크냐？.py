import sys
input = sys.stdin.readline

while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    if n > m:
        sys.stdout.write("Yes" + "\n")
    else:
        sys.stdout.write("No" + "\n")