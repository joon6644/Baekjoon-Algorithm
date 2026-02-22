import sys
input = sys.stdin.readline

N = int(input())
A = int(''.join(input().split()))
B = int(''.join(input().split()))

print(min(A, B))