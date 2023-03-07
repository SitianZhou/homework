# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys

import sys

count = 0
mylist = []

for i in range(1,len(sys.argv)):
	count += 1 # Count
	mylist.append(float(sys.argv[i]))

# total
total = sum(mylist)
# find mean	
mean = total/count
mylist.sort()

# find median
mid_pos = len(mylist)//2
if len(mylist)%2 == 1:
	median = mylist[mid_pos]
else:
	median = (mylist[mid_pos-1] + mylist[mid_pos])/2

# sd
squared_tot = 0
for i in range(1,len(sys.argv)):
	squared_tot += (float(sys.argv[i])-mean)**2
	sd = (squared_tot / count)**0.5
	
# output
print(f'Count: {count}')
print(f'Minimum: {mylist[0]}')
print(f'Maximum: {mylist[-1]}')
print(f'Mean: {mean:.3f}')
print(f'Std. dev: {sd:.3f}')
print(f'Median: {median:.3f}')

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
