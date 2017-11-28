# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


import sys

def solution():
	# define an infinite number for n
	n = sys.maxint
	for i in xrange(1, n):
		if (i % 1 == 0 
			and i % 2 == 0 
			and i % 3 == 0 
			and i % 4 == 0 
			and i % 5 == 0 
			and i % 6 == 0 
			and i % 7 == 0 
			and i % 8 == 0 
			and i % 9 == 0 
			and i % 10 == 0
			and i % 11 == 0 
			and i % 12 == 0 
			and i % 13 == 0 
			and i % 14 == 0 
			and i % 15 == 0 
			and i % 16 == 0 
			and i % 17 == 0 
			and i % 18 == 0 
			and i % 19 == 0 
			and i % 20 == 0):
				break 

	return i

# how should I rewrite this code in a nicer format?
def solution():
	for i in xrange(1, sys.maxint):
		# for x in range(10):
		# 	if all(i % x == 0):

		# if i % {0}.format(range(11))== 0:
			break

	return i


if __name__ == "__main__":
	print solution()