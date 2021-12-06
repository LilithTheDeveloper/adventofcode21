import os.path

number_lines = []

with open('adventofcode21\day1\input.txt') as f:
    lines = f.readlines()
    lines = [line.rstrip() for line in lines]
    number_lines = [int(x) for x in lines]

increments = 0
sum_window_A = 0
sum_window_B = 0

for i in range(0, len(number_lines)-3):
    sum_window_A = number_lines[i] + number_lines[i+1] + number_lines[i+2]
    sum_window_B = number_lines[i+1] + number_lines[i+2] + number_lines[i+3]
    if sum_window_A < sum_window_B:
        increments = increments + 1

print(increments)