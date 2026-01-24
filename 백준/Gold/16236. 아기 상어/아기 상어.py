import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')

# 시작 좌표를 받아서 먹이의 위치와 거리를 반환하는 함수
def search(start):
    r, c = start[0], start[1]
    queue = deque([start])
    visited = {(r, c)}
    candidates = []
    min_dist = INF
    space[r][c] = 0

    while queue:
        curr_r, curr_c, dist = queue.popleft()   

        if dist >= min_dist:
            continue

        for i in range(4):
            next_r = curr_r + dr[i]
            next_c = curr_c + dc[i]

            if not (0 <= next_r < N and 0 <= next_c < N):
                continue
            if (next_r, next_c) in visited:
                continue
            if space[next_r][next_c] > shark_size:
                continue
            
            if space[next_r][next_c] > 0 and space[next_r][next_c] < shark_size:
                min_dist = dist + 1
                candidates.append((next_r, next_c, min_dist))

            visited.add((next_r, next_c))
            queue.append((next_r, next_c, dist + 1))
        
    if candidates:
        candidates.sort()
        return candidates[0]
    else:
        return None
            
N = int(input())

space = []
start = (-1, -1, -1)

for r in range(N):
    line = list(map(int, input().split()))

    for c in range(N):
        if start != (-1, -1, -1):
            break
        if line[c] == 9:
            start = (r, c, 0)
    space.append(line)

dr = [-1, 0, 1, 0]
dc = [0, -1, 0, 1]

shark_size = 2
eat_count = 0
total_time = 0

while True:
    result = search(start)
    
    if result is None: break
        
    r, c, time = result
    
    total_time += time
    start = (r, c, 0)

    eat_count += 1
    if eat_count == shark_size:
        shark_size += 1
        eat_count = 0

print(total_time)