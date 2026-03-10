"""
Problem Statement: Given an array size N+1 with elements between 1 and N, find the duplicate.
"""

def find_duplicate(nums):
    slow = fast = nums[0]
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    return slow

#Amit Kumar 202310101150190