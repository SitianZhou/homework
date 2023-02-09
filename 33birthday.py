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
total = 0
for n in range(10000):
	mylist = []
	found = 0
	for i in range(int(sys.argv[2])):
		r = random.randint(1,int(sys.argv[1]))
		mylist.append(r)
	
	for j in range(len(mylist)):
		for k in range(j+1, len(mylist)):
			if mylist[j] == mylist[k]:
				found = 1
				break
	total += found
prob = total / 10000
print(f'{prob:.3f}')


"""
python3 33birthday.py 365 23
0.571
"""

