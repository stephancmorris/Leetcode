"""
LeetCode 25. Reverse Nodes in k-Group
Difficulty: Hard
Category: Linked List

Given the head of a linked list, reverse the nodes of the list k at a time, and return the 
modified list.
k is a positive integer and is less than or equal to the length of the linked list. If the 
number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
You may not alter the values in the list's nodes, only nodes themselves may be changed.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseKGroup(head, k):
    """
    Reverse nodes in groups of k.
    
    Args:
        head: Head of linked list
        k: Group size for reversal
        
    Returns:
        Head of modified linked list
    """
    # TODO: Implement your solution here
    pass
