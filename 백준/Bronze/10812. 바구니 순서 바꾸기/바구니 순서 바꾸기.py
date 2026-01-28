import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())

queue = deque([x for x in range(1, N + 1)])

for _ in range(M):
    i, j, k = map(int, input().split())
    pop_list = []

    queue.rotate(1 - i)

    for _ in range(k - i):
        pop_list.append(queue.popleft())

    queue.rotate(N - j + i - 1)
    queue.extend(pop_list)
    queue.rotate(j - N)

print(*queue)