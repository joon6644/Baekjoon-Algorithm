import sys
from collections import deque
input = sys.stdin.readline
INF = float('inf')

def search(start):
    flag = True
    size = [2, 0]
    total_time = 0

    while flag:
        flag = False
        queue = deque([start])
        visited = set(start)
        records = []
        st_dist = INF
        space[start[0]][start[1]] = 0

        while queue:
            curr_r, curr_c, time = queue.popleft()   
            if time >= st_dist:
                continue

            for i in range(4):
                next_r = curr_r + dr[i]
                next_c = curr_c + dc[i]

                if not (0 <= next_r < N and 0 <= next_c < N):
                    continue
                if (next_r, next_c) in visited:
                    continue
                if space[next_r][next_c] > size[0]:
                    continue
                
                if space[next_r][next_c] > 0 and space[next_r][next_c] < size[0]:
                    flag = True
                    records.append((next_r, next_c))
                    st_dist = time + 1

                visited.add((next_r, next_c))
                queue.append((next_r, next_c, time + 1))
        
        if flag:
            records.sort()
            r, c = records[0]
            
            total_time += st_dist
            start = (r, c, 0)

            size[1] += 1
            if size[1] == size[0]:
                size[0] += 1
                size[1] = 0 

    return total_time
            
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

ans = search(start)

print(ans)