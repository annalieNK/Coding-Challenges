# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

def search_arr(arr, target):
	for i in range(0, len(arr)):
		if arr[i] == target:
			return i
	return -1


arr = [4, 5, 6, 7, 1, 3, 2]
print search_arr(arr, 3) 
