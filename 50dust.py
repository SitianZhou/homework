#!/usr/bin/env python3

# 50dust.py

# Write a better version of your 42dust.py program
# Your program must have the following properties

# 1. has option and default value for window size
# 2. has option and default value for entropy threshold
# 3. has a switch for N-based or lowercase (soft) masking
# 4. works with uppercase or lowercase input files
# 5. works as an executable

# Optional: make the algorithm faster (see 29gcwin.py for inspiration)
# Optional: benchmark your programs with different window sizes using time

# Hint: make a smaller file for testing (e.g. e.coli.fna in the CLI below)

import mcb185
import math
import argparse

parser = argparse.ArgumentParser(description='Entropy filter')
parser.add_argument('file', type=str, metavar='<path>', help='some file')
parser.add_argument('-w', required=False, type=int, default = 11,
	metavar='<int>', help='required integer argument')
parser.add_argument('-t', required=False, type=float, default = 1.4,
	metavar='<float>', help='required floating point argument')
parser.add_argument('-s', action='store_true', 
	help='on/off lowercase masking')
arg = parser.parse_args()

# entropy filter
def entropy_filter(seq, win, threshold):
	c_a = 0
	c_c = 0
	c_g = 0
	c_t = 0

	for nt in seq:
		if nt == "A" or nt == "a":   c_a += 1
		elif nt == "C" or nt == "c": c_c += 1
		elif nt == "G" or nt == "g": c_g += 1
		elif nt == "T" or nt == "t": c_t += 1
	prob_list = [c_a/win, c_c/win, c_g/win, c_t/win]
	h = 0
	for p_i in prob_list: 
		if p_i == 0: continue
		h -= p_i*math.log2(p_i)
	if h < threshold: filter = True
	else:             filter = False
	return filter
# convert seq to uppercase and save it to a new seq
myseq = ''
for defline, seq in mcb185.read_fasta(arg.file):
	seq_2 = seq.upper()
	# convert windows w/ entropy lower than threshold to Ns/lowercase
	for i in range(len(seq)-arg.w):
		if entropy_filter(seq[i:i+arg.w], arg.w, arg.t):
			if arg.s:
				sub_seq = seq[i:i+arg.w].lower()
				seq_2 = seq_2[:i] + sub_seq + seq_2[i+arg.w:]
			else: seq_2 = seq_2[:i] + "N"*arg.w + seq_2[i+arg.w:]
		else: continue
	# output
	print(f'>{defline}')
	for i in range(0,len(seq_2),60):
		print(seq_2[i:i+60])
	

"""
python3 50dust.py -w 11 -t 1.4 -s e.coli.fna  | head
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGcttttcattctGACTGCAACGGGCAATATGTCTCTGTGTggattaaaaaaagagtgTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGagtaaattaaaattttattgaCTTAGG
TCACtaaatactttaaCCAATATAGGCATAGCGCACAGacagataaaaattacaGAGTac
acaacatccaTGAAACGCATTAGCACCACCATtaccaccaccatcaccaTTACCACAGGT
AACggtgcgggctgACGCGTACAGgaaacacagaaaaaagccCGCACCTGACAGTGCggg
ctttttttttcgaCCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
AggcaggggcaggtggCCAccgtcctctctgcccccgccaaaatcaccaaccacctGGTG
GCGATgattgaaaaaaccattaGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
"""
