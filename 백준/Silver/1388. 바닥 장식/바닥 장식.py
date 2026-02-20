import sys
input = sys.stdin.readline

N, M = map(int, input().split())
floor = [input().rstrip() for _ in range(N)]

count = 0

for i in range(N):
    for j in range(M):
        if floor[i][j] == '-':
            if j == 0 or floor[i][j-1] != '-':
                count += 1

for j in range(M):
    for i in range(N):
        if floor[i][j] == '|':
            if i == 0 or floor[i-1][j] != '|':
                count += 1

print(count)