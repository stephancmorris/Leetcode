"""
LeetCode 124. Binary Tree Maximum Path Sum
Difficulty: Hard
Category: Trees

A path in a binary tree is a sequence of nodes where each pair of adjacent nodes in the 
sequence has an edge connecting them. A node can only appear in the sequence at most once. 
Note that the path does not need to pass through the root.
The path sum of a path is the sum of the node's values in the path.
Given the root of a binary tree, return the maximum path sum of any non-empty path.

Time Complexity: O(n)
Space Complexity: O(h) where h is height of tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root):
    """
    Find maximum path sum in binary tree.
    
    Args:
        root: Root of binary tree
        
    Returns:
        Maximum path sum
    """
    # TODO: Implement your solution here
    pass
