# 31entropy.py

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()

# Hint: try breaking your program with erroneous input

import sys
import math

prob_list = []

for val in range(1,len(sys.argv)):
	prob_list.append(float(sys.argv[val]))

# check if all command line values are numbers
for val in prob_list:
	try: num = float(val)
	except: raise
# check if all numbers sum to 1
assert(sum(prob_list) == 1)


H = 0
for i in range(len(prob_list)):
	p_i = prob_list[i]
	H -= p_i*math.log2(p_i)


print(f'{H:.3f}')

"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
