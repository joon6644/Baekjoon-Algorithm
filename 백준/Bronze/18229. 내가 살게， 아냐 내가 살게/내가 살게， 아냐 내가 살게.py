import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())

ans = [0, float('inf')]  # 번호, 횟수

for i in range(1, N + 1):
    row = map(int, input().split())
    val = 0
    for idx, j in enumerate(row):
        idx += 1
        val += j
        if val >= K and idx < ans[1]:
            ans = [i, idx]
            break

print(*ans)