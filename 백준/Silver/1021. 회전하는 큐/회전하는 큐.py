import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))

queue = deque([x for x in range(1, N + 1)])
length = N
ans = 0
for item in A:
    cnt = 0
    while queue[0] != item:
        queue.rotate(-1)
        cnt += 1
    
    queue.popleft()
    length -= 1
    
    if 2 * cnt <= length:
        ans += cnt
    else:
        ans += length - cnt + 1

print(ans)