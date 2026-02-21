import sys

N = int(sys.stdin.readline())

for i in range(1, N + 1):
    strings = input().split()
    
    rev_strings = " ".join(strings[::-1])
    
    sys.stdout.write(f"Case #{i}: {rev_strings}" + "\n")