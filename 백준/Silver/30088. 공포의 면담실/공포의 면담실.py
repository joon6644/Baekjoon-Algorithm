import sys

input_data = sys.stdin.read().split()
n = int(input_data[0])
idx = 1

dept_total_times = []

for _ in range(n):
    emp_count = int(input_data[idx])
    dept_sum = sum(map(int, input_data[idx+1 : idx+1+emp_count]))
    dept_total_times.append(dept_sum)
    idx += 1 + emp_count
    
dept_total_times.sort()

total_wait_time = 0
current_sum = 0

for time in dept_total_times:
    current_sum += time
    total_wait_time += current_sum
    
print(total_wait_time)