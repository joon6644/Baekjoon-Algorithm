import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())

    t = []
    for i in range(1, (n + 1) // 2):
        t.append(f"{i} {n - i}")

    sys.stdout.write(f"Pairs for {n}: {', '.join(t)}\n")