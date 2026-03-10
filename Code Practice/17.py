"""
Problem: Find the missing number in range [0, n].
Input: [3, 0, 1] -> Output: 2
"""

def missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum

#Amit Kumar 202310101150190