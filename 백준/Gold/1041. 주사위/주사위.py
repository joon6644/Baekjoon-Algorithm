import sys
input = sys.stdin.readline

N = int(input())

dice = list(map(int, input().split()))

if N == 1:
    print(sum(sorted(dice)[:5]))
    sys.exit()

f = 5 * N**2 - 16 * N + 12
e = 8 * N - 12  
v = 4

nums = []
for i in range(3):
    nums.append(min(dice[i], dice[5 - i]))
nums.sort()
for i in range(2):
    nums[i + 1] += nums[i]

print(f * nums[0] + e * nums[1] + v * nums[2])