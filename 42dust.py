# 42dust.py

# Write a program that performs entropy filtering on nucleotide fasta files
# Windows that are below the entropy threshold are replaced by N

# Program arguments include file, window size, and entropy threshold

# Output should be a fasta file with sequence wrapped at 60 characters

# Hint: use the mcb185 library
# Hint: make up some fake sequences for testing

# Note: don't worry about "centering" the entropy on the window (yet)

import mcb185
import sys
import math

file = sys.argv[1]
win = int(sys.argv[2])
threshold = float(sys.argv[3])

def entropy_calc(seq):
	c_a = 0
	c_c = 0
	c_g = 0
	c_t = 0

	for nt in seq:
		if nt == "A":   c_a += 1
		elif nt == "C": c_c += 1
		elif nt == "G": c_g += 1
		else:           c_t += 1
	prob_list = [c_a/len(seq), c_c/len(seq), c_g/len(seq), c_t/len(seq)]
	h = 0
	for p_i in prob_list: 
		if p_i == 0: continue
		h -= p_i*math.log2(p_i)
	return h


myseq = ''
for defline, seq in mcb185.read_fasta(file):
	for i in range(0, len(seq), win):
		myseq += seq[i:i+win]

# converting windows w/ entropy lower than the threshold to N
for i in range(len(myseq)):
	if entropy_calc(seq[i:i+win]) < threshold:
		myseq = myseq[:i] + "N"*win + myseq[i+win:]
	else: continue

# output
print(f'>{defline}')
for i in range(0,len(myseq),60):
	print(myseq[i:i+60])


"""
python3 42dust.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 11 1.4
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGNNNNNNNNNNNGACTGCAACGGGCAATATGTCTCTGTGTNNNNNNNNNNNNNNNNNTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGNNNNNNNNNNNNNNNNNNNNNCTTAGG
TCACNNNNNNNNNNNNCCAATATAGGCATAGCGCACAGNNNNNNNNNNNNNNNNGAGTNN
NNNNNNNNNNTGAAACGCATTAGCACCACCATNNNNNNNNNNNNNNNNNTTACCACAGGT
AACNNNNNNNNNNNACGCGTACAGNNNNNNNNNNNNNNNNNNCGCACCTGACAGTGCNNN
NNNNNNNNNNNNNCCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
ANNNNNNNNNNNNNNNCCANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNGGTG
GCGATNNNNNNNNNNNNNNNNNGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
...
"""
