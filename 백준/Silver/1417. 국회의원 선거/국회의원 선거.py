import sys
import heapq
input = sys.stdin.readline

def solve():
    n = int(input())
    dasom = int(input())

    if n == 1:
        print(0)
        return
    
    others = []
    for _ in range(n - 1):
        heapq.heappush(others, -int(input()))

    count = 0
    while others:
        max_votes = -heapq.heappop(others)

        if dasom > max_votes:
            break

        dasom += 1
        max_votes -= 1
        count += 1

        heapq.heappush(others, -max_votes)

    print(count)

if __name__ == '__main__':
    solve()