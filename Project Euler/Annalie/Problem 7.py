# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10001st prime number?

import sys

def solution(y):

	n = sys.maxint

	"""Find the prime numbers for n"""
	primenumbers = []
	for i in xrange(2, n):
		for x in xrange(2, i):
			if i % x == 0:
				# i is not a prime number
				break
		# get the prime numbers instead
		else: 
			primenumbers.append(i)

		"""Stop when the list contains of y numbers"""
		if len(primenumbers) == y:
			break

	"""Print the last number of the list"""
	return max(primenumbers)


if __name__ == "__main__":
	print solution(10001)