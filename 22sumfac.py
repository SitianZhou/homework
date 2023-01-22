# 22sumfac.py

# Write a program that computes the running sum from 1..n
# Also, have it compute the factorial of n while you're at it
# Use the same loop for both calculations

# Note: you may not import math or any other library

SUM = 0
FACT = 1
n = 5
for i in range(1, n+1):
	SUM += i
	FACT *= i
print(n, SUM, FACT)

"""
python3 22sumfac.py
5 15 120
"""
