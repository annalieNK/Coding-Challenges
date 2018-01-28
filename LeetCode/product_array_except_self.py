# Given an array of n integers where n > 1, nums, 
# return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

# Solve it without division and in O(n).

# For example, given [1,2,3,4], return [24,12,8,6]

arr = [1,2,3,4]


def product_except_self(arr):
        p = arr[0]
        n = len(arr)
        prod = []

        for i in range(0, len(arr)):
            prod.append(p)
            p = p * arr[i]
        
        # p = arr[0]
        # for i in range(len(arr)-1, -1, -1):
        #     prod[i] = prod[i] * p
        #     p = p * arr[i]
        
        return prod

print product_except_self(arr)


# prod = [1] * len(arr)
# pi = arr[0]
# pj = arr[0]

# for i in range(len(arr)):
#     j = -1-i

#     prod[i] *= pi
#     prod[j] *= pj
#     pi *= arr[i]
#     pj *= arr[j]        
            
# return prod