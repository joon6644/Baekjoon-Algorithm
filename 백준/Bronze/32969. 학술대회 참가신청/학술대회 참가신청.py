import sys

p = {'bigdata', 'public', 'society'}

N = sys.stdin.readline().split()

for i in N:
    if i in p:
        print("public bigdata")
        sys.exit()

print("digital humanities")