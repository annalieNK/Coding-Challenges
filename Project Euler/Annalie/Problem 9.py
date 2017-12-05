# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a**2 + b**2 = c**2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def solution(n):

	for c in xrange(1, n):
		for b in xrange(1, c-1):
			for a in xrange(1, b-1):
				if a + b + c == n and a**2 + b**2 == c**2:
					print 'a: {}, b: {}, c: {}'.format(a, b, c)
					return a * b * c


if __name__ == "__main__":
	print solution(1000)

