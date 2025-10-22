"""
LeetCode 138. Copy List with Random Pointer
Difficulty: Medium
Category: Linked List

A linked list of length n is given such that each node contains an additional random pointer, 
which could point to any node in the list, or null.
Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, 
where each new node has its value set to the value of its corresponding original node. Both 
the next and random pointer of the new nodes should point to new nodes in the copied list such 
that the pointers in the original list and copied list represent the same list state.

Time Complexity: O(n)
Space Complexity: O(n)
"""

# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

def copyRandomList(head):
    """
    Create deep copy of linked list with random pointers.
    
    Args:
        head: Head of original linked list
        
    Returns:
        Head of copied linked list
    """
    # TODO: Implement your solution here
    pass
