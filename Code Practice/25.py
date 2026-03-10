"""
Given two integer arrays nums1 and nums2, return an array of their intersection. [cite: 270]
Each element in the result must be unique. [cite: 271]
Logic: Use a hash map to track elements seen in the first array.
"""

def intersection(nums1, nums2):
    seen = {}
    for n in nums1:
        seen[n] = True
        
    res = []
    for n in nums2:
        if n in seen:
            res.append(n)
            del seen[n]
    return res

#Amit Kumar 202310101150190