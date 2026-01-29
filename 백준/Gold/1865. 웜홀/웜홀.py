import sys
input = sys.stdin.readline

TC = int(input())

for _ in range(TC):
    N, M, W = map(int, input().split())

    dist = [0] * (N + 1)
    edges = []
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append((S, E, T))
        edges.append((E, S, T))
    
    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append((S, E, -T))

    flag = True
    for i in range(N):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w 

                if i == N - 1:
                    flag = False
                  
    if flag:
        print("NO")
    else:
        print("YES")