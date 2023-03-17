# 71gff.py

# Write a program that converts genes in gff into JSON
# Use the minaturized version of the C. elegans genome (included) this time
# Organize the genes onto chromosomes
# Print the number of genes on each chromosome to stderr
# Your code should mimic the output below

# Hint: your outer data structure is a dictionary

# Note: gene names are stored differently here than the last file

import gzip
import sys
import re
import json

filename = sys.argv[1]
dict = {}
genelist = []
chr_count = {}

with gzip.open(filename, 'rt') as fp:
	for line in fp.readlines():
		for match in re.finditer('ID=Gene', line):
			# count genes on each chr
			chr_match = re.search('\w+', line)
			chr = chr_match.group()
			if chr not in chr_count:
				chr_count[chr] = 0
			chr_count[chr] += 1
			
			genedict = {}
			# gene name
			name_match = re.search('sequence_name=(\S+?);', line)
			name = name_match.group(1)
			# coordinates
			pos_match = re.search('(\d+)\s+(\d+)', line)
			beg = int(pos_match.group(1))
			end = int(pos_match.group(2))
			# strand
			str_match = re.search('(\.\s+)(.)(\s+\.)', line)
			strand = str_match.group(2)
			
			genedict["gene"] = name
			genedict["beg"] = beg
			genedict["end"] = end
			genedict["strand"] = strand
			if chr not in dict:
				dict[chr] = []
			dict[chr].append(genedict)

fp.close()


for chr in chr_count:
	print(chr, chr_count[chr])

print(json.dumps(dict, indent=4))


"""
python3 71gff.py elegans
I 37
II 57
III 37
IV 41
MtDNA 2
V 41
X 45
{
    "I": [
        {
            "gene": "Y74C9A.6",
            "beg": 3747,
            "end": 3909,
            "strand": "-"
        },
        {
            "gene": "Y74C9A.3",
            "beg": 4116,
            "end": 10230,
            "strand": "-"
        },
...
"""
