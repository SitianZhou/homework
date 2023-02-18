# 41transmembrane.py

# Write a program that predicts which proteins in a proteome are transmembrane

# Transmembrane proteins are characterized by having
#    1. a hydrophobic signal peptide near the N-terminus
#    2. other hydrophobic regions to cross the plasma membrane

# Both the signal peptide and the transmembrane domains are alpha-helices
# Therefore, they do not contain Proline

# Hydrophobicity can be measured by Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot

# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

# Hint: copy mcb185.py to your homework repo and import that
# Hint: create a function for KD calculation
# Hint: create a function for hydrophobic alpha-helix
# Hint: use the same function for both signal peptide and transmembrane



import mcb185
import sys

def KD_calc(seq):
	total = 0
	for aa in seq:
		if aa == 'A': total += 1.8
		elif aa == 'C': total += 2.5
		elif aa == 'D': total += -3.5
		elif aa == 'E': total += -3.5
		elif aa == 'F': total += 2.8
		elif aa == 'G': total += -0.4
		elif aa == 'H': total += -3.2
		elif aa == 'I': total += 4.5
		elif aa == 'K': total += -3.9
		elif aa == 'L': total += 3.8
		elif aa == 'M': total += 1.9
		elif aa == 'N': total += -3.5
		elif aa == 'P': total += -1.6
		elif aa == 'Q': total += -3.5
		elif aa == 'R': total += -4.5
		elif aa == 'S': total += -0.8
		elif aa == 'T': total += -0.7
		elif aa == 'V': total += 4.2
		elif aa == 'W': total += -0.9
		elif aa == 'Y': total += -1.3
	kd = total / len(seq)
	return kd


def h_phob_alpha_helix(seq, kd_threshold):
	if KD_calc(seq) > kd_threshold:
		is_h_phob = True
	else: is_h_phob = False
	
	for aa in seq:
		is_alpha_helix = True
		if  aa == 'P' :
			is_alpha_helix = False
			break
	
	if is_h_phob == True and is_alpha_helix == True:
		is_h_phob_alpha_helix = True
	else: is_h_phob_alpha_helix = False
	
	return is_h_phob_alpha_helix

# signal peptide
for defline, seq in mcb185.read_fasta(sys.argv[1]):
	if len(seq) <= 30: continue
	win = 8
	signal = False
	for i in range(0,30-win):
		if h_phob_alpha_helix(seq[i:i+win], 2.5) == True:
			signal = True
			break
		else: continue

	# transmembrane region
	win = 11
	transmembrane = False
	for i in range(30, len(seq)-win):
		if h_phob_alpha_helix(seq[i:i+win], 2) == True:
			transmembrane = True
			break
		else: continue
		
	if signal == True and transmembrane == True: print(defline)






"""
python3 41transmembrane.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
NP_414560.1 Na(+):H(+) antiporter NhaA [Escherichia coli str. K-12 substr. MG1655]
NP_414568.1 lipoprotein signal peptidase [Escherichia coli str. K-12 substr. MG1655]
NP_414582.1 L-carnitine:gamma-butyrobetaine antiporter [Escherichia coli str. K-12 substr. MG1655]
NP_414607.1 DedA family protein YabI [Escherichia coli str. K-12 substr. MG1655]
NP_414609.1 thiamine ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414653.1 protein AmpE [Escherichia coli str. K-12 substr. MG1655]
NP_414666.1 quinoprotein glucose dehydrogenase [Escherichia coli str. K-12 substr. MG1655]
NP_414695.1 iron(III) hydroxamate ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414699.1 PF03458 family protein YadS [Escherichia coli str. K-12 substr. MG1655]
NP_414717.2 CDP-diglyceride synthetase [Escherichia coli str. K-12 substr. MG1655]
...
"""
