# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers

import random

AT_counts = 0
total = 0
mystring = ""
seq = 30


for i in range(seq):
	r = random.random()
	if r < 0.6:
		mystring += random.choice('AT')
		AT_counts += 1
		total += 1
	else:
		mystring += random.choice('CG')
		total += 1

AT_content = AT_counts / total

print(len(mystring), AT_content, mystring)

"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
