import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())

for x in range(1, 11):
    results = []
    for y in range(1, 11):
        if A * x + B * y == C:
            results.append(y)
    
    if results:
        print(*(sorted(results)))
    else:
        print(0)