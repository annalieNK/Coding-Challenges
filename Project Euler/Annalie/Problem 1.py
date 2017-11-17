# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
# The sum of these multiples is 23.

# Find the sum of all the multiples of 3 or 5 below 1000.

#### Solution
# create a list of all the numbers below 1000 that can be divided by 3 or 5
# create one list to prevent counting some outcomes twice
# get the sum of the numbers in this list


def solution(n):
	result = []
	for i in range(n):
		if i % 3 == 0 or i % 5 == 0:
			# print i
			result.append(i)
	return sum(result)


def solution_list(n):
	result = [x for x in range(n) if x % 3 == 0 or x % 5 == 0]
	return sum(result)


if __name__ == "__main__":
	print solution_list(1000)
