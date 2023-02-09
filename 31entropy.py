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
H = 0

for i in range(1,len(sys.argv)):
	prob_list.append(float(sys.argv[i]))
	p_i = float(sys.argv[i])
	H -= p_i*math.log2(p_i)

assert(sum(prob_list) == 1) # make sure prob sum to 1
print(f'{H:.3f}')

"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
