"""
LeetCode 102. Binary Tree Level Order Traversal
Difficulty: Medium
Category: Trees

Given the root of a binary tree, return the level order traversal of its nodes' values. 
(i.e., from left to right, level by level).

Time Complexity: O(n)
Space Complexity: O(w) where w is maximum width of tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root):
    """
    Perform level order traversal of binary tree.
    
    Args:
        root: Root of binary tree
        
    Returns:
        List of lists, each containing values at a level
    """
    # TODO: Implement your solution here
    pass
