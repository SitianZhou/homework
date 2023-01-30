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
seq = 30

import random

for i in range(seq):
	r = random.randint(1,10)
	if r == 1 or r == 2 or r == 3:
		mystring += 'A'
	elif r == 4 or r == 5 or r == 6:
		mystring += 'T'
	elif r == 7 or r == 8:
		mystring += 'C'
	else:
		mystring += 'G'

for n in range(len(mystring)):
	if mystring[n] == 'A' or mystring[n] == 'T':
		AT_counts += 1
		total += 1
	else:
		total += 1
		
AT_content = AT_counts / total

print(len(mystring), AT_content, mystring)

"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
