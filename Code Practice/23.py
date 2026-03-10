"""
Problem: Move all 0's to the end while maintaining order. In-place.
"""

def move_zeros(nums):
    pos = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1

#Amit Kumar 202310101150190