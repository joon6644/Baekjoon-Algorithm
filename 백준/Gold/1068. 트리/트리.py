import sys
input = sys.stdin.readline

N = int(input())
parent = list(map(int, input().split()))
D = int(input())
parent[D] = -99

root = -99
childs = [[] for _ in range(N)]
for cur, par in enumerate(parent):
    if par == -1:
        root = cur
        continue
    if par == -99:
        continue
    childs[par].append(cur)

if root == -99:
    print(0)
    sys.exit()
    
stack = [root]
cnt = 0
while stack:
    curr = stack.pop()
    if not childs[curr]:
        cnt += 1
        continue

    for next in childs[curr]:
        stack.append(next)

print(cnt)