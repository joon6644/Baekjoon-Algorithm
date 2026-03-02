import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
lab = []
empty = []
virus = []

for i in range(N):
    row = list(map(int, input().split()))
    lab.append(row)
    for j in range(M):
        if row[j] == 0:
            empty.append((i, j))
        elif row[j] == 2:
            virus.append((i, j))

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

max_val = 0

for walls in combinations(empty, 3):
    copy_lab = [row[:] for row in lab] 
    val = len(empty) - 3
    
    for r, c in walls:
        copy_lab[r][c] = 1
    
    queue = deque(virus)
    
    while queue:
        r, c = queue.popleft()

        if val <= max_val:
            break

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if not(0 <= nr < N and 0 <= nc < M):
                continue

            if copy_lab[nr][nc] == 0:
                copy_lab[nr][nc] = -1
                val -= 1

                queue.append((nr, nc))

    if val > max_val:           
        max_val = val

print(max_val)