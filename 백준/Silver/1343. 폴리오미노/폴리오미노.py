import sys
input = sys.stdin.readline

X = input().rstrip() + "."

A = "AAAA"
B = "BB"
ans = []

start = 0
for idx, char in enumerate(X):

    if char == ".":
        ans.append(char)
        if start != -1:
        
            l = idx - start
            if l % 2 != 0:
                print(-1)
                sys.exit()

            a, b = l // 4, (l % 4) // 2
            ans.append(A * a)
            ans.append(B * b)
        
            start = -1

    if char == "X" and start == -1:
        start = idx

print(''.join(ans[1:]))