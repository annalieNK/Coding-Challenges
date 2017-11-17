# Each new term in the Fibonacci sequence is generated by adding the previous two terms. 
# By starting with 1 and 2, the first 10 terms will be:

# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

# By considering the terms in the Fibonacci sequence whose values do not exceed four million, 
# find the sum of the even-valued terms.


# Frist try an example for values that do not exceed 100.

#### Solution
# create a list of the Fibonacci sequence of which the values are smaller than 10, starting with 1 and 2
# create a new list that only contains the even-values
# sum the values in the new list

def solution(n):
	fibseq = []
	fibseqeven = []
	a, b = 1, 2
	while a < n:
		fibseq.append(a)
		a, b = b, a + b
	for i in fibseq:
		if i % 2 == 0:
			fibseqeven.append(i)
	return sum(fibseqeven)



if __name__ == "__main__":
	print solution(4000000)
