import sys
import heapq
input = sys.stdin.readline
INF = float('inf')

def dijkstra(start_node, end_node):
    distance = [INF] * (N + 1)
    distance[start_node] = 0
    heap = []
    heapq.heappush(heap, (0, start_node))

    while heap:
        curr_cost, curr_node = heapq.heappop(heap)

        if curr_cost > distance[curr_node]:
            continue

        for next_cost, next_node in graph[curr_node]:
            total_cost = next_cost + curr_cost

            if total_cost >= distance[next_node]:
                continue

            distance[next_node] = total_cost
            heapq.heappush(heap, (total_cost, next_node))

    return distance[end_node]

N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((c, b))
v1, v2 = map(int, input().split())

print(dijkstra(v1, v2))