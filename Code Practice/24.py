"""
Problem: Return the element that appears more than n/2 times.
"""

def majority_element(nums):
    candidate = None
    count = 0
    for n in nums:
        if count == 0:
            candidate = n
        count += 1 if n == candidate else -1
    return candidate

#Amit Kumar 202310101150190