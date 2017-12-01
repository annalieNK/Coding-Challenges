# The sum of the squares of the first ten natural numbers is,

# 1**2 + 2**2 + ... + 10**2 = 385

# The square of the sum of the first ten natural numbers is,

# (1 + 2 + ... + 10)**2 = 552 = 3025

# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 minus 385 is 2640.

# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def solution(n):

	# function for sum of the squares of the first ten natural numbers
	squares = []
	for i in range(1,n):
		squares.append(i**2)
		i += 1
		sumsquares = sum(squares)

	# function for the square of the sum of the first ten natural numbers
	squaresum = sum(range(1,n))**2

	# difference between sum of the squeares and the square of the sum
	return squaresum - sumsquares


if __name__ == "__main__":
	print solution(101)