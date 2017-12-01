# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


import sys

def create_range_optim(n):
	divisors = range(1, n+1)
	for i in divisors:
		[divisors.remove(x) for x in divisors if i % x == 0 and x != i]
	return divisors

def solution():
	divisors = create_range_optim(20)
	# define an infinite number for n
	n = sys.maxint
	for i in xrange(1, n):
		if all([i % x == 0 for x in divisors]):
			break
	return i

# # how should I rewrite this code in a nicer format?
# def solution():
# 	for i in xrange(1, sys.maxint):
# 		# for x in range(10):
# 		# 	if all(i % x == 0):

# 		# if i % {0}.format(range(11))== 0:
# 			break

# 	return i


if __name__ == "__main__":
	print solution()