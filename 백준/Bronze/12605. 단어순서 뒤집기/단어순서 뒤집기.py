import sys
input = sys.stdin.readline

N = int(input())

for i in range(1, N + 1):
    strings = input().split()

    sys.stdout.write("Case #" + str(i) + ": ")
    for j in strings[::-1]:
        sys.stdout.write(j + " ")
    print()