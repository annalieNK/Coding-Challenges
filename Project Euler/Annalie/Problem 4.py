# A palindromic number reads the same both ways. 
# The largest palindrome made from the product of two 2-digit numbers is 9009  91  99.
# Find the largest palindrome made from the product of two 3-digit numbers.


# compute the result for each a x b
# where a and b consist of three digits
# convert the integer value to a string value
# for each result, check whether the last and the first values are the same AND 
# where the second and the fifth digit are the same AND 
# where the third and the fourth digit are the same
# convert the string value back to an integer value
# print the max value


def solution(n):
	
	# create list of all possible outcomes of three digit numbers
	outcomes = []
	for a in range(100,n):
		for b in range(100,n):
			outcomes.append(a*b)
	outcomes = list(set(outcomes))

	# convert integers in list to strings
	outcomes_str = [str(i) for i in outcomes]

	# find palidromes
	palindromes = []
	for i in outcomes_str:
		if i[0] == i[-1] and i[1] == i[-2] and i[2] == i[-3]:
			palindromes.append(i)

	# convert strings back to integers
	palindromes_int = [int(i) for i in palindromes]

	# print the largest palindrome
	return max(palindromes_int)


if __name__ == "__main__":
	print solution(1000)