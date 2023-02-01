# 29gcwin.py

# Write a program that computes the GC fraction of a DNA sequence in windows
# Window size is 11 nt
# Output with 4 significant figures
# Try this with nested loops first

# Variation: try programming this without nested loops
# Instead, count only the first window
# Then 'move' the window by adding 1 letter on one side
# And subtracting 1 letter from the other side
# Consider the pros/cons of this algorithm vs. nested loops
import math

seq = 'ACGACGCAGGAGGAGAGTTTCAGAGATCACGAATACATCCATATTACCCAGAGAGAG'
w = 11
x = len(seq)

# calculating GC content
for i in range(0, x-w+1):
	CG_counts = 0
	for j in range(i , i + w):
		if seq[j] == "C" or seq[j] == "G":
			CG_counts += 1
		else:
			continue
	CG_content = CG_counts / w

	# round to 4 sig fig
	y = CG_content*10000 - int(CG_content*10000)
	print(i, seq[i:j+1], end = ' ')
	if y < 0.5: print(math.floor(CG_content*10000)/10000)
	else:       print(math.ceil(CG_content*10000)/10000)


"""
python3 26gcwin.py
0 ACGACGCAGGA 0.6364
1 CGACGCAGGAG 0.7273
2 GACGCAGGAGG 0.7273
3 ACGCAGGAGGA 0.6364
4 CGCAGGAGGAG 0.7273
5 GCAGGAGGAGA 0.6364
6 CAGGAGGAGAG 0.6364
7 AGGAGGAGAGT 0.5455
8 GGAGGAGAGTT 0.5455
9 GAGGAGAGTTT 0.4545
10 AGGAGAGTTTC 0.4545
11 GGAGAGTTTCA 0.4545
12 GAGAGTTTCAG 0.4545
13 AGAGTTTCAGA 0.3636
14 GAGTTTCAGAG 0.4545
15 AGTTTCAGAGA 0.3636
16 GTTTCAGAGAT 0.3636
17 TTTCAGAGATC 0.3636
18 TTCAGAGATCA 0.3636
19 TCAGAGATCAC 0.4545
20 CAGAGATCACG 0.5455
21 AGAGATCACGA 0.4545
22 GAGATCACGAA 0.4545
23 AGATCACGAAT 0.3636
24 GATCACGAATA 0.3636
25 ATCACGAATAC 0.3636
26 TCACGAATACA 0.3636
27 CACGAATACAT 0.3636
28 ACGAATACATC 0.3636
29 CGAATACATCC 0.4545
30 GAATACATCCA 0.3636
31 AATACATCCAT 0.2727
32 ATACATCCATA 0.2727
33 TACATCCATAT 0.2727
34 ACATCCATATT 0.2727
35 CATCCATATTA 0.2727
36 ATCCATATTAC 0.2727
37 TCCATATTACC 0.3636
38 CCATATTACCC 0.4545
39 CATATTACCCA 0.3636
40 ATATTACCCAG 0.3636
41 TATTACCCAGA 0.3636
42 ATTACCCAGAG 0.4545
43 TTACCCAGAGA 0.4545
44 TACCCAGAGAG 0.5455
45 ACCCAGAGAGA 0.5455
46 CCCAGAGAGAG 0.6364
"""
