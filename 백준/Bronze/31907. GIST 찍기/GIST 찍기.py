import sys

data = ["G...", ".I.T", "..S."]

K = int(sys.stdin.readline())

for i in data:
    line = []
    
    for char in i:
        line.append(char * K)
    
    for _ in range(K):
        sys.stdout.write(''.join(line) + "\n")