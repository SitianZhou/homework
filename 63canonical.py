# 63canonical.py

# You probably learned that ATG is the only start codon, but is it?
# Write a program that reports the start codons from the E. coli genome
# Your program must:
#    1. read GCF_000005845.2_ASM584v2_genomic.gbff.gz at the only input
#    2. use a regex to find CDS coordinates
#    3. count how many different start codons there are

# Note: the sequence is at the end of the file
# Note: genes on the negative strand are marked complement(a..b)

# Hint: you can read a file twice, first to get the DNA, then the CDS
# Hint: check your CDS by examining the source protein

import gzip
import sys
import re

filename = sys.argv[1]

def r_dna(dna):
	rdna = ""
	for i in range(len(dna)-1, -1, -1):
		if dna[i] == 'A':
			rdna += 'T'
		elif dna[i] == 'T':
			rdna += 'A'
		elif dna[i] == 'C':
			rdna += 'G'
		elif dna[i] == 'G':
			rdna += 'C'
		else: rdna += 'N'
	return rdna

seq = ""

# get the DNA
with gzip.open(filename, 'rt') as fp:
	for line in fp.readlines():
		if re.search("\s\s\d+\s[acgt]+", line): 
			for match in re.finditer("[acgt]+", line):
				seq += match.group().upper()
fp.close()

# get CDS
count = {}
with gzip.open(filename, 'rt') as fp:
	for line in fp.readlines():
		# forward strand
		if re.search('CDS\s+\d+..\d+', line):
			match = re.search('(\d+)..(\d+)', line)
			start = seq[int(match.group(1))-1:int(match.group(1))+2]
			if start not in count:
				count[start] = 0
			count[start] += 1

		elif re.search('CDS\s+join', line):
			match = re.search('(\d+)..(\d+)', line)
			start = seq[int(match.group(1))-1:int(match.group(1))+2]
			if start not in count:
				count[start] = 0
			count[start] += 1
		
		# reverse strand
		elif re.search('CDS\s+complement\(\d+', line):
			match = re.search('(\d+)..(\d+)', line)
			start = r_dna(seq[int(match.group(2))-3:int(match.group(2))])
			if start not in count:
				count[start] = 0
			count[start] += 1
			
		elif re.search('CDS\s+complement\(join', line):
			match = re.search('(\d+)..(\d+)', line)
			start = r_dna(seq[int(match.group(2))-3:int(match.group(2))])
			if start not in count:
				count[start] = 0
			count[start] += 1
			
				
fp.close()

for start in count:
	print(start, count[start])

"""
python3 63canonical.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.gbff.gz
ATG 3883
GTG 338
TTG 80
ATT 5
AGT 1
AAA 1
AGC 1
TTC 1
TAA 1
CGT 1
CTG 2
GAC 1
"""
