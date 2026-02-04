import sys
from datetime import datetime, timedelta

input_data = sys.stdin.readline().split()
date_str = input_data[0]
N = int(input_data[1])

start_date = datetime.strptime(date_str, "%Y-%m-%d")

target_date = start_date + timedelta(days=N-1)

print(target_date.strftime("%Y-%m-%d"))