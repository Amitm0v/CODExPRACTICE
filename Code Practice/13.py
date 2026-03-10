"""
Problem: Given a collection of intervals, merge all overlapping intervals.
Input: [[1,3],[2,6],[8,10],[15,18]]
"""

def merge_intervals(intervals):
    if not intervals:
        return []
    intervals.sort()
    merged = [intervals[0]]
    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)
    return merged

#Amit Kumar 202310101150190