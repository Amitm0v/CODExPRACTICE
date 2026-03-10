"""
Given an integer array nums and an integer k, return the kth largest element. [cite: 150]
Logic: Partition the array similar to QuickSort to find the pivot at index k.
"""

def find_kth_largest(nums, k):
    k = len(nums) - k
    
    def quick_select(l, r):
        pivot, p = nums[r], l
        for i in range(l, r):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[r] = nums[r], nums[p]
        
        if p > k: return quick_select(l, p - 1)
        elif p < k: return quick_select(p + 1, r)
        else: return nums[p]
        
    return quick_select(0, len(nums) - 1)

#Amit Kumar 202310101150190