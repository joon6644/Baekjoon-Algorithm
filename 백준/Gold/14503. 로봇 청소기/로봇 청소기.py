import sys
input = sys.stdin.readline

N, M = map(int, input().split())
r, c, d = map(int, input().split())

room = []
for _ in range(N):
    room.append(list(map(int, input().split())))

robot = [r, c, d]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cnt = 0
while True:
    r, c, d = robot
    if room[r][c] == 0:
        room[r][c] = -1
        cnt += 1

    is_clean = True
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if not (0 <= nr < N and 0 <= nc < M):
            continue
        if room[nr][nc] == 0:
            is_clean = False
            break
            
    if is_clean:
        nd = (d + 2) % 4
        nr = r + dr[nd]
        nc = c + dc[nd]

        if not (0 <= nr < N and 0 <= nc < M):
            break
        if room[nr][nc] != 1:
            robot = [nr, nc, d]
            continue
        else: break

    else:
        for i in range(4):
            nd = (d - i - 1) % 4
            nr = r + dr[nd]
            nc = c + dc[nd]

            if not (0 <= nr < N and 0 <= nc < M):
                continue
            if room[nr][nc] == 0:
                robot = [nr, nc, nd]
                break
        continue

print(cnt)