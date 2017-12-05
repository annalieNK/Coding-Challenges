# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.


def solution(n):

	sieve = [True]*n
	a = 0
	for i in xrange(2, n):
		if sieve[i]:
			a += i
			for x in xrange(i*i, n, i):
				sieve[x] = False
	return a

if __name__ == "__main__":
	print solution(2000000)