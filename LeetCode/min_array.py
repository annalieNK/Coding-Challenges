# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# Find the minimum element.

# You may assume no duplicate exists in the array.


def min_array(arr):

	# set first element as the minimum value
	min_element = arr[0]

	for i in arr:

		min_element = min(min_element, i)

	return min_element


arr = [4, 5, 6, 7, 1, 3, 2]
print min_array(arr)