#### Largest prime factor 

# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143?


#### Solution
# create list of prime numbers: numbers that can only be divided by itself or by 1
# select the numbers from the list that multiplied together make the original number, n:
	# create a list of the prime numbers that return no left overs for n, n % prime number == 0 
	# select the largest prime number from this list


def solution(n):
	"""Find the prime numbers for n"""
	primenumbers = []
	for i in range(2, n):
		for x in range(2, i):
			if i % x == 0:
				# i is not a prime number
				break
		# get the prime numbers instead
		else: 
			primenumbers.append(i)

	"""Create a list of the prime numbers that return no left overs for n"""
	primenumbers = find_prime_numbers(n)
	primenumbers_selection = []
	for i in primenumbers:
		if n % i == 0:
			primenumbers_selection.append(i)

	"""Return max value from list"""
	return max(primenumbers_selection)


if __name__ == "__main__":
	print solution(13195)