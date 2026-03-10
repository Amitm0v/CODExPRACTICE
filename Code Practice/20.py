"""
Given an integer array nums, rotate the array to the right by k steps. [cite: 207]
Logic: Reverse the whole array, then reverse the first k, then reverse the rest.
"""

def rotate_array(nums, k):
    n = len(nums)
    k %= n
    
    def reverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
            
    reverse(0, n - 1)
    reverse(0, k - 1)
    reverse(k, n - 1)

#Amit Kumar 202310101150190