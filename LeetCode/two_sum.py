# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1]


arr = [11, 2, 15, 7]

def two_sum(arr, target):
	for i in range(0, len(arr)):
		for j in range(i + 1, len(arr)):
			if arr[i] + arr[j] == target:
				return [i, j]

print two_sum(arr, 9)