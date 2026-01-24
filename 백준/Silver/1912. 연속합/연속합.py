import sys
input = sys.stdin.readline

n = int(input())
array = [0] + list(map(int, input().split()))

for i in range(1, n + 1):
    array[i] += array[i - 1]

max_val = array[1]
min_val = 0
for i in range(1, n + 1):
    val = array[i] - min_val

    if val > max_val:
        max_val = val
    
    if array[i] < min_val:
        min_val = array[i]

print(max_val)