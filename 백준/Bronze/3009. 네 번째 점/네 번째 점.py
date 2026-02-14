import sys
input = sys.stdin.readline

X, Y = [], []

for _ in range(3):
    x, y = map(int, input().split())
    if x in X:
        X.pop(X.index(x))
    else:
        X.append(x)

    if y in Y:
        Y.pop(Y.index(y))
    else:
        Y.append(y)
    
print(X[0], Y[0])