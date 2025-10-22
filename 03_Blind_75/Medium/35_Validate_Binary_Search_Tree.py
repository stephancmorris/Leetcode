"""
LeetCode 98. Validate Binary Search Tree
Difficulty: Medium
Category: Trees

Given the root of a binary tree, determine if it is a valid binary search tree (BST).
A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Time Complexity: O(n)
Space Complexity: O(h) where h is height of tree
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root):
    """
    Check if binary tree is a valid BST.
    
    Args:
        root: Root of binary tree
        
    Returns:
        Boolean indicating if tree is valid BST
    """
    # TODO: Implement your solution here
    pass
