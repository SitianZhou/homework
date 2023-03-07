# 32xcoverage.py

# Write a program that simulates a shotgun resequencing project
# How uniformly do the reads "pile up" on a chromosome?
# How much of that depends on sequencing depth?

# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line

# Hint: make the problem smaller, so it's easier to visualize and debug
# Hint: if you don't understand the context of the problem, ask for help
# Hint: if you are undersampling the ends, do something about it

# Note: you will not get exactly the same results as the command line below

import sys
import random

genome_size = int(sys.argv[1])
read_num = int(sys.argv[2])
read_len = int(sys.argv[3])

seq = [0]*genome_size
for i in range(read_num):
	r = random.randint(0, genome_size-read_len)
	for j in range(0, read_len):
		seq[r+j] += 1

print(f'{min(seq[read_len-1:-(read_len-1)])}', end = ' ')
print(f'{max(seq[read_len-1:-(read_len-1)])}', end = ' ')
print(f'{sum(seq[read_len-1:-(read_len-1)])/(genome_size-2*(read_len-1)):.7}')


"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
