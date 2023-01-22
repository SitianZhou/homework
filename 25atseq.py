# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers

AT_counts = 0
total = 0
mystring = ""

import random
mylist = ['A', 'T', 'C', 'G']
seq = random.choices(mylist, weights = [3, 3, 2, 2], k = 30) # 60% AT
for n in range(len(seq)):
	if seq[n] == 'A' or seq[n] == 'T':
		AT_counts += 1
		total += 1
		mystring += seq[n]
	else:
		total += 1
		mystring += seq[n]

AT_content = AT_counts / total

print(len(mystring), AT_content, mystring)

"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
