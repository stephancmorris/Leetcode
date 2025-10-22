"""
LeetCode 105. Construct Binary Tree from Preorder and Inorder Traversal
Difficulty: Medium
Category: Trees

Given two integer arrays preorder and inorder where preorder is the preorder traversal of a 
binary tree and inorder is the inorder traversal of the same tree, construct and return the binary tree.

Time Complexity: O(n)
Space Complexity: O(n)
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder, inorder):
    """
    Construct binary tree from preorder and inorder traversals.
    
    Args:
        preorder: Preorder traversal array
        inorder: Inorder traversal array
        
    Returns:
        Root of constructed binary tree
    """
    # TODO: Implement your solution here
    pass
