import sys
input = sys.stdin.readline

N = int(input())

for i in range(1, N + 1):
    strings = input().split()
    
    rev_strings = " ".join(strings[::-1])
    
    print(f"Case #{i}: {rev_strings}")