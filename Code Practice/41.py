"""
Problem: Return the middle node (or second middle if even length).
"""

def find_middle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow

#Amit Kumar 202310101150190