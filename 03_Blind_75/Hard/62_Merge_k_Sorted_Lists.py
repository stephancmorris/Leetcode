"""
LeetCode 23. Merge k Sorted Lists
Difficulty: Hard
Category: Linked List

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Time Complexity: O(n log k) where n is total number of nodes
Space Complexity: O(log k) for recursion stack
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    """
    Merge k sorted linked lists.
    
    Args:
        lists: Array of k sorted linked lists
        
    Returns:
        Merged sorted linked list
    """
    # TODO: Implement your solution here
    pass
