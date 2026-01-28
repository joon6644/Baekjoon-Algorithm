import sys
input = sys.stdin.readline

K = int(input())

S = [x for x in input().rstrip()]

for i in range(K, len(S), 2 * K):
    S[i:i+K] = S[i:i+K][::-1]
    
ans = []

i = 0
while i != K:
    for j in range(i, len(S), K):
        ans.append(S[j])
    i += 1

print(''.join(ans))