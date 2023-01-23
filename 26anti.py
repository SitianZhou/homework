# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna = 'ACTGAAAAAAAAAAA'
x = len(dna)
mystring = ''

for n in range(x):
	if dna[x - 1 - n] == 'A':
		mystring += 'T'
	elif dna[x - 1 - n] == 'T':
		mystring += 'A'
	elif dna[x -1 - n] == 'C':
		mystring += 'G'
	elif dna[x - 1 - n] == 'G':
		mystring += 'C'
print(mystring)

"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
