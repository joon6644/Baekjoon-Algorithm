import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())

    t = [f"{i} {n - i}" for i in range(1, (n + 1) // 2)]

    sys.stdout.write(f"Pairs for {n}: {', '.join(t)}\n")