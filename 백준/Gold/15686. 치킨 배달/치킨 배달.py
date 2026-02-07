import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())

house = []
chicken = []

# 1. 치킨집 리스트와 집 리스트에 모든 좌표를 저장한다
for r in range(N):
    line = map(int, input().split())
    for c, item in enumerate(line):
        if item == 1:
            house.append((r, c))
        elif item == 2:
            chicken.append((r, c))

min_city_dist = float('inf')

# 2. 조합을 사용하여 계산할 모든 치킨집의 경우의수를 순회하여 뽑는다
for team in combinations(chicken, M):
    city_dist = 0

    # 3. 집의 입장에서 가장 가까운 치킨집에 대한 정보로 갱신하여 반영한다
    for hx, hy in house:
        min_dist = float('inf')
        for cx, cy in team:
            dist = abs(hx - cx) + abs(hy - cy)
            min_dist = min(min_dist, dist)
        city_dist += min_dist

        if city_dist >= min_city_dist:
            break

    # 4. 각 케이스에 대해 최소값을 갱신하며 답을 찾는다
    min_city_dist = min(min_city_dist, city_dist)

print(min_city_dist)