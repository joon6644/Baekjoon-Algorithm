import sys
input = sys.stdin.readline

n = int(input())

if n == 1 or n == 3:
    print(-1)

elif n % 5 == 0:  # 5, 10, 15
    print(n // 5)

elif n % 5 == 1:  # 6, 11, 16
    print((n // 5) - 1 + 3)

elif n % 5 == 2:  # 7, 12, 17
    print((n // 5) + 1)

elif n % 5 == 3:  # 8, 13, 18
    print((n // 5) - 1 + 4)

elif n % 5 == 4:  # 9, 14, 19
    print((n // 5) + 2)