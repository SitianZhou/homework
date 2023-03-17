# 70gff.py

# Write a program that converts genes in gff into JSON
# Use the E. coli genome gff
# Your code should mimic the output below

import json
import re
import sys
import gzip

filename = sys.argv[1]

genelist = []

with gzip.open(filename, 'rt') as fp:
	for line in fp.readlines():
		if line.startswith('#'): continue
		for match in re.finditer('RefSeq\s+gene', line):
			dict = {}
			# gene name
			name = re.search('(Name=)(\w+)', line)
			gene = name.group(2)
			dict["gene"] = gene
			# start/stop position
			pos_match = re.search('(\d+)\s+(\d+)', line)
			beg = int(pos_match.group(1))
			end = int(pos_match.group(2))
			dict["beg"] = beg
			dict["end"] = end
			# strand
			str_match = re.search('(\.\s+)(.)(\s+\.)', line)
			strand = str_match.group(2)
			dict["strand"] = strand
			
			genelist.append(dict)	
fp.close()

print(json.dumps(genelist, indent=4))




"""
python3 70gff.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.gff.gz
[
    {
        "gene": "thrL",
        "beg": 190,
        "end": 255,
        "strand": "+"
    },
    {
        "gene": "thrA",
        "beg": 337,
        "end": 2799,
        "strand": "+"
    },
...
"""
