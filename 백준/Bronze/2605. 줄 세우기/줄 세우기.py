import sys
input = sys.stdin.readline

n = int(input())
tickets = list(map(int, input().split()))

line = []
for i in range(n):
    student_num = i + 1
    ticket = tickets[i]
    
    insert_idx = len(line) - ticket
    line.insert(insert_idx, student_num)

print(*line)