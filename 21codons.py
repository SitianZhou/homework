# 21codons.py

# Print out all the codons for the sequence below in reading frame 1

# Hint: use the slice operator

dna = 'ATAGCGAATATCTCTCATGAGAGGGAA'

for n in range(0,len(dna),3):
	x = slice(n, 3+n, 1)
	print(dna[x])

"""
python3 21codons.py
ATA
GCG
AAT
ATC
TCT
CAT
GAG
AGG
GAA
"""
