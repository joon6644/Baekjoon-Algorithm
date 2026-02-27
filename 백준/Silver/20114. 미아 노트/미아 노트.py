import sys
input = sys.stdin.readline

N, H, W = map(int, input().split())

ans = ['?'] * N

for _ in range(H):
    line = input().rstrip()

    for i in range(N):
        if ans[i] != '?':
            continue

        for j in range(i*W, i*W+W):
            if line[j] != '?':
                ans[i] = line[j]
                break

print(''.join(ans))