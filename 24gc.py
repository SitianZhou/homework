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

print(f'{CG_content:.2f}')





"""
python3 24gc.py
0.42
"""
