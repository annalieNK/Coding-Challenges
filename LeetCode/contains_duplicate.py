# Given an array of integers, find if the array contains any duplicates. 
# Your function should return true if any value appears at least twice in the array, 
# and it should return false if every element is distinct.


def contains_duplicate(arr):

	if len(arr) < 2:
		return "array has only one element"

	if len(arr) == len(set(arr)):
		return "false"
	else: 
		return "true"

arr = [1,1,3,4,5]
print contains_duplicate(arr)