"""
LeetCode 112. Path Sum
Difficulty: Medium
Category: Trees

Given the root of a binary tree and an integer targetSum, return true if the tree has a 
root-to-leaf path such that adding up all the values along the path equals targetSum.
A leaf is a node with no children.

Time Complexity: O(n)
Space Complexity: O(h) where h is height of tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root, targetSum):
    """
    Check if tree has root-to-leaf path with target sum.
    
    Args:
        root: Root of binary tree
        targetSum: Target sum to find
        
    Returns:
        Boolean indicating if path exists
    """
    # TODO: Implement your solution here
    pass
