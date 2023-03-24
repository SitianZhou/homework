#Write a program the reads in a FASTA file and reports the following information:

#Number of sequences
#Total length
#Shortest sequence
#Longest sequence
#Median sequence length
#N50 length
#Composition of each letter in the sequence

import sys
import mcb185

filename = sys.argv[1]

# number of seq, total len, shortest, longest
stat = []
seq_count = 0
nt_count = {}
total = 0
for defline, seq in mcb185.read_fasta(filename):
	myseq = seq.upper() # so it works with both upper and lowercase input
	stat.append(len(myseq))
	seq_count += 1
	total += len(myseq)
	for nt in myseq:
		if nt not in nt_count:
			nt_count[nt] = 0
		nt_count[nt] += 1

# median
stat.sort()
m_pos = len(stat)//2
if len(stat)%2 == 1:
	median = stat[m_pos]
else:
	median = (stat[m_pos-1] + stat[m_pos])/2


# N50
length = sum(stat)
l = 0
for i in range(len(stat)-1, -1, -1):
	l += stat[i]
	if l >= length/2:
		N50 = stat[i]
		break

# output
print(f'Number of sequence: {seq_count}')
print(f'Total length: {total}')
print(f'Shortest sequence length: {stat[0]}')
print(f'Longest sequence length: {stat[-1]}')
print(f'Median length: {median}')
print(f'N50 length: {N50}')
# composition
print(f'Nucleotide composition:')
for nt in nt_count:
	print(f'{nt} {nt_count[nt]/total:.4f}')
