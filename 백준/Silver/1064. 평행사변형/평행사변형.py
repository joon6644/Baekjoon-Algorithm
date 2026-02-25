import sys
import math

input = sys.stdin.readline

xa, ya, xb, yb, xc, yc = map(int, input().split())

if (xb - xa) * (yc - ya) == (yb - ya) * (xc - xa):
    print(-1.0)
else:
    ab = math.sqrt((xb - xa)**2 + (yb - ya)**2)
    bc = math.sqrt((xc - xb)**2 + (yc - yb)**2)
    ca = math.sqrt((xa - xc)**2 + (ya - yc)**2)

    lengths = [ab, bc, ca]
    max_diff = 2 * (max(lengths) - min(lengths))
    
    print(max_diff)