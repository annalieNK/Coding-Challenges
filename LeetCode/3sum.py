# Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? 
# Find all unique triplets in the array which gives the sum of zero.

# Note: The solution set must not contain duplicate triplets.

# For example, given array S = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [[-1, 0, 1],
#  [-1, -1, 2]]

def sum_3(arr, target):
	solutions = []
	arr = list(set(arr))

	for i in range(0, len(arr)):
		for j in range(i + 1, len(arr)):
			for k in range(i + 2, len(arr)):
				if arr[i] + arr[j] + arr[k] == target:
					solutions.append([arr[i], arr[j], arr[k]])
					
	return solutions


def sum_3(arr, target):
	solutions = []
	solutions2 = []

	for i in range(0, len(arr)):
		for j in range(i + 1, len(arr)):
			for k in range(i + 2, len(arr)):
				if arr[i] + arr[j] + arr[k] == target:
					solutions.append(sorted([arr[i], arr[j], arr[k]]))
					
	for l in solutions:
		if l not in solutions2:
			solutions2.append(l)

	return solutions2


arr = [-1, 0, 1, 2, -1, -4]
# arr = [-1, 2, 1, -1, 0, -4]
# arr =[-1, -1, 0, 2, 1, -4]

print sum_3(arr, 0)

