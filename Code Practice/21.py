"""
Problem: Find a subarray that has the largest product.
"""

def max_product(nums):
    res = max(nums)
    cur_min, cur_max = 1, 1
    for n in nums:
        temp = cur_max * n
        cur_max = max(n * cur_max, n * cur_min, n)
        cur_min = min(temp, n * cur_min, n)
        res = max(res, cur_max)
    return res

#Amit Kumar 202310101150190