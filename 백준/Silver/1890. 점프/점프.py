import sys
input = sys.stdin.readline

N = int(input())
board = []
for _ in range(N):
    line = map(int, input().split())
    board.append(list([x, 0] for x in line))

board[0][0][1] = 1

for r in range(N):
    for c in range(N):
        if r == N - 1 and c == N - 1:
            break

        jump = [board[r][c][0], 0]

        for i in range(2):
            nr = r + jump[i]
            nc = c + jump[i - 1]

            if not (0 <= nr < N and 0 <= nc < N):
                continue

            board[nr][nc][1] += board[r][c][1]

print(board[N - 1][N - 1][1])