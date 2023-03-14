# 62orfs.py

# Make a program that finds open reading frames in the E. coli genome
# Your program should read a fasta file
# There should be an optional minimum ORF size with a default value of 300 nt
# The output should be a table showing 4 columns
#     1. parent sequence identifier
#     2. begin coordinate
#     3. end coordinate
#     4. strand
#     5. first 10 amino acids of the protein

# Hint: use argparse, mcb185.read_fasta(), and mcb185.translate()
# Hint: don't use the whole genome for testing

# Note: your genes should be similar to those in the real genome

import argparse
import mcb185
import re

parser = argparse.ArgumentParser(description='find orfs')
parser.add_argument('file', type=str, metavar='<path>', help='some file')
arg = parser.parse_args()

# find reverse strand
def rev_seq(seq):
	rseq = ""
	for i in range(len(seq)-1, -1, -1):
		if seq[i] == 'A':
			rseq += 'T'
		elif seq[i] == 'T':
			rseq += 'A'
		elif seq[i] == 'C':
			rseq += 'G'
		elif seq[i] == 'G':
			rseq += 'C'
		else: rseq += 'N'
	return rseq

# find orfs in the forward strand
def orfs(seq, frame=0, min=300):
	i = frame
	while i < len(seq):
		codon = seq[i:i+3]
		if codon == "ATG":
			for j in range(i+3, len(seq), 3):
				codon = seq[j:j+3]
				if codon == "TAA" or codon == "TAG" or codon == "TGA":
					if j-i > min:
						yield i+1, j+3, mcb185.translate(seq[i:j+2])
					i = j
					break
		i += 3

# find orfs in the reverse strand
def rev_orfs(seq, frame=0, min=300):
	i = frame
	while i < len(seq):
		codon = rseq[i:i+3]
		if codon == "ATG":
			for j in range(i+3, len(seq), 3):
				codon = rseq[j:j+3]
				if codon == "TAA" or codon == "TAG" or codon == "TGA":
					if j-i > min:
						yield len(seq)-j-2,len(seq)-i,mcb185.translate(rseq[i:j+2])
					i = j
					break
		i += 3

# sort & output
for defline, seq in mcb185.read_fasta(arg.file):
	match = re.search('\w+.\w+', defline)
	rseq = rev_seq(seq)
	info = {}
	for frame in range(3):
		for start, end, aaseq in orfs(seq, frame=frame):
			info[start] = f'{end} + {aaseq[:10]}'
		for start, end, aaseq in rev_orfs(rseq, frame=frame):
			info[start] = f'{end} - {aaseq[:10]}'

for start in sorted(pos):
	print(match.group(), start, info[start])

	

"""
python3 62orfs.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz
NC_000913.3 108 500 - MVFSIIATRW
NC_000913.3 337 2799 + MRVLKFGGTS
NC_000913.3 2801 3733 + MVKVYAPASS
NC_000913.3 3512 4162 - MSHCRSGITG
NC_000913.3 3734 5020 + MKLYNLKDHN
NC_000913.3 3811 4119 - MVTGLSPAIW
NC_000913.3 5310 5738 - MKIPPAMANW
NC_000913.3 5683 6459 - MLILISPAKT
NC_000913.3 6529 7959 - MPDFFSFINS
NC_000913.3 7366 7773 + MKTASDCQQS
"""
