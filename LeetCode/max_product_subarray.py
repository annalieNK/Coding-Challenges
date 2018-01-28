# Find the contiguous subarray within an array (containing at least one number) which has the largest product.

# For example, given the array [2,3,-2,4],
# the contiguous subarray [2,3] has the largest product = 6.

arr = [2,3,-2,4]

def max_prod_subarr(arr):
	# set previous sum as the first integer
	max_prod = arr[0]
	current_prod = arr[0]

	for i in arr[1:]:

		# find the highest current product
		current_prod = max(current_prod*i, i)
		# print current_prod

		# set the new max product as the max of this current products
		max_prod = max(current_prod, max_prod)


	return max_prod

print max_prod_subarr(arr)