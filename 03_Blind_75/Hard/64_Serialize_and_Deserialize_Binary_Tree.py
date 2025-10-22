"""
LeetCode 297. Serialize and Deserialize Binary Tree
Difficulty: Hard
Category: Trees

Serialization is the process of converting a data structure or object into a sequence of bits 
so that it can be stored in a file or memory buffer, or transmitted across a network connection 
link to be reconstructed later in the same or another computer environment.
Design an algorithm to serialize and deserialize a binary tree. There is no restriction on 
how your serialization/deserialization algorithm should work. You just need to ensure that a 
binary tree can be serialized to a string and this string can be deserialized to the original 
tree structure.

Time Complexity: O(n) for both operations
Space Complexity: O(n) for both operations
"""

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    def serialize(self, root):
        """
        Encodes a tree to a single string.
        
        Args:
            root: Root of binary tree
            
        Returns:
            Serialized string representation
        """
        # TODO: Implement your solution here
        pass

    def deserialize(self, data):
        """
        Decodes your encoded data to tree.
        
        Args:
            data: Serialized string representation
            
        Returns:
            Root of reconstructed binary tree
        """
        # TODO: Implement your solution here
        pass
