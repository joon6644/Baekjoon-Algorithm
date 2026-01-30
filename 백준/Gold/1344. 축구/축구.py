import sys
from math import comb
input = sys.stdin.readline

P_A = int(input()) / 100
P_B = int(input()) / 100

P = [P_A, P_B]

# 정답 = 1 - (둘 다 소수득점이 아닌 경우)
# 경기는 90분, 5분 간격으로 끊으면 18번

# 18개의 칸 중 소수(2, 3, 5, 7, 11, 13, 17)를 제외한 개수를 순회하며 경우의 수 계산
# sum(확률을 고른 칸 수만큼 제곱 * 각 경우의수) -> 소수득점이 아닌 확률

# B에도 적용 후 둘의 곱을 1에서 빼주기

nums = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18]
probs = [0, 0]
for x in range(2):
    for i in nums:
        p_i = comb(18, i)
        
        probs[x] += p_i * P[x]**i * (1 - P[x])**(18 - i)

print(1 - probs[0] * probs[1])