# 24gc.py

# Write a program that computes the GC% of a DNA sequence
# Format the output for 2 decimal places
import math

dna = 'ACAGAGCCAGCAGATATACAGCAGATACTAT'

CG_counts = 0
total = 0
for n in range(len(dna)):
	if dna[n] == 'C' or dna[n] == 'G':
		CG_counts += 1
		total += 1
	else: 
		total += 1

CG_content = CG_counts / total

# rounding
x = CG_content*100 - int(CG_content*100)
if x < 0.5: print(math.floor(CG_content*100)/100)
else:        print(math.ceil(CG_content*100)/100)




"""
python3 24gc.py
0.42
"""
