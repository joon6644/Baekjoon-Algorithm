import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

p_c = B // A
p_w = p_c * 3
ans = p_w * C

print(ans)