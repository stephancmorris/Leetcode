"""
LeetCode 100. Same Tree
Difficulty: Easy
Category: Trees

Given the roots of two binary trees p and q, write a function to check if they are the same or not.
Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

Time Complexity: O(min(m, n))
Space Complexity: O(min(m, n))
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
    """
    Check if two binary trees are identical.
    
    Args:
        p: Root of first binary tree
        q: Root of second binary tree
        
    Returns:
        Boolean indicating if trees are identical
    """
    # TODO: Implement your solution here
    pass
