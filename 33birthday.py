# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list

import sys
import random

input_list = []
for val in range(1,len(sys.argv)):
	input_list.append(int(sys.argv[val]))


total = 0
for n in range(100000):
	days = [0]*input_list[0]
	found = 0
	for i in range(input_list[1]):
		r = random.randint(0,input_list[0]-1)
		if days[r] == 0:
			days[r] += 1
		else:
			found = 1
			break
	total += found

prob = (total/100000)
print(f'{prob:.3f}')


"""
python3 33birthday.py 365 23
0.571
"""

