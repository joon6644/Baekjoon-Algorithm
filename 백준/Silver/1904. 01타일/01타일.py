import sys
input = sys.stdin.readline

N = int(input())

a = 1
b = 2

if N == 1:
    print(1)
    sys.exit()

# 마지막이 1로 끝나거나 00으로 끝나거나. 
# 1로 끝나면 i-1의 개수, 00으로 끝나면 i-2의 개수

for i in range(3, N + 1):
    a, b = b, (a + b) % 15746

print(b)