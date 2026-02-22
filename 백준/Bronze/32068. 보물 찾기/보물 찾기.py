import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    L, R, S = map(int, input().split())

    if abs(L - S) >= abs(R - S): # 오른쪽 승리
        sys.stdout.write(f"{abs(R - S) * 2}\n")
    else: # 왼쪽 승리
        sys.stdout.write(f"{abs(L - S) * 2 + 1}\n")