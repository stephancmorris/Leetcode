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


# Test cases
def test_validate_binary_search_tree():
    """Test cases for Validate Binary Search Tree"""
    test_cases = [
        # Basic test cases
        (create_tree1(), True),   # [2,1,3]
        (create_tree2(), False),  # [5,1,4,null,null,3,6]
        (create_tree3(), True),   # [1]
        (create_tree4(), False),  # [5,4,6,null,null,3,7]
        
        # Edge cases
        (None, True),             # Empty tree
        (create_single_node(), True),  # Single node
        (create_tree5(), False),  # [2,2,2] - duplicates
        (create_tree6(), True),   # [1,null,1] - valid
        (create_tree7(), False),  # [1,1] - invalid
        
        # LeetCode test cases
        (create_tree1(), True),   # [2,1,3]
        (create_tree2(), False),  # [5,1,4,null,null,3,6]
        
        # Additional test cases
        (create_tree8(), True),   # [10,5,15,null,null,6,20]
        (create_tree9(), False),  # [10,5,15,null,null,6,20] with invalid 6
        (create_tree10(), True),  # [0]
        (create_tree11(), False), # [1,1]
        (create_tree12(), True),  # [2,1,3]
        (create_tree13(), False), # [5,1,4,null,null,3,6]
        
        # Large numbers
        (create_tree14(), True),  # [1000000000, -1000000000, 1000000000]
        (create_tree15(), False), # [1000000000, -1000000000, 1000000000] invalid
        
        # Negative numbers
        (create_tree16(), True),  # [-1, -2, -3]
        (create_tree17(), False), # [-1, -2, -3] invalid
    ]
    
    print("Testing Validate Binary Search Tree solution...")
    for i, (root, expected) in enumerate(test_cases):
        result = isValidBST(root)
        if result == expected:
            print(f"✓ Test {i+1} passed: result={result}")
        else:
            print(f"✗ Test {i+1} failed")
            print(f"  Expected: {expected}, Got: {result}")
    
    print("\nAll tests completed!")


# Helper functions for creating trees
def create_tree1():
    """Create tree [2,1,3] - valid BST"""
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    return root

def create_tree2():
    """Create tree [5,1,4,null,null,3,6] - invalid BST"""
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    return root

def create_tree3():
    """Create tree [1] - valid BST"""
    return TreeNode(1)

def create_tree4():
    """Create tree [5,4,6,null,null,3,7] - invalid BST"""
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(6)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(7)
    return root

def create_single_node():
    """Create single node tree"""
    return TreeNode(1)

def create_tree5():
    """Create tree [2,2,2] - invalid BST with duplicates"""
    root = TreeNode(2)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    return root

def create_tree6():
    """Create tree [1,null,1] - valid BST"""
    root = TreeNode(1)
    root.right = TreeNode(1)
    return root

def create_tree7():
    """Create tree [1,1] - invalid BST"""
    root = TreeNode(1)
    root.left = TreeNode(1)
    return root

def create_tree8():
    """Create tree [10,5,15,null,null,6,20] - valid BST"""
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(20)
    return root

def create_tree9():
    """Create tree [10,5,15,null,null,6,20] - invalid BST"""
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(20)
    return root

def create_tree10():
    """Create tree [0] - valid BST"""
    return TreeNode(0)

def create_tree11():
    """Create tree [1,1] - invalid BST"""
    root = TreeNode(1)
    root.left = TreeNode(1)
    return root

def create_tree12():
    """Create tree [2,1,3] - valid BST"""
    root = TreeNode(2)
    root.left = TreeNode(1)
    root.right = TreeNode(3)
    return root

def create_tree13():
    """Create tree [5,1,4,null,null,3,6] - invalid BST"""
    root = TreeNode(5)
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root.right.left = TreeNode(3)
    root.right.right = TreeNode(6)
    return root

def create_tree14():
    """Create tree [1000000000, -1000000000, 1000000000] - valid BST"""
    root = TreeNode(1000000000)
    root.left = TreeNode(-1000000000)
    root.right = TreeNode(1000000000)
    return root

def create_tree15():
    """Create tree [1000000000, -1000000000, 1000000000] - invalid BST"""
    root = TreeNode(1000000000)
    root.left = TreeNode(-1000000000)
    root.right = TreeNode(1000000000)
    return root

def create_tree16():
    """Create tree [-1, -2, -3] - valid BST"""
    root = TreeNode(-1)
    root.left = TreeNode(-2)
    root.right = TreeNode(-3)
    return root

def create_tree17():
    """Create tree [-1, -2, -3] - invalid BST"""
    root = TreeNode(-1)
    root.left = TreeNode(-2)
    root.right = TreeNode(-3)
    return root


# Performance test
def test_performance():
    """Test solution performance with large tree"""
    import time
    
    # Generate large BST
    large_tree = create_large_bst(1000)
    
    start_time = time.time()
    result = isValidBST(large_tree)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large BST (1000 nodes): {end_time - start_time:.4f} seconds")
    print(f"Result: {result}")


def create_large_bst(n):
    """Create a large BST with n nodes"""
    if n == 0:
        return None
    
    root = TreeNode(n // 2)
    root.left = create_large_bst(n // 2)
    root.right = create_large_bst(n - n // 2 - 1)
    return root


if __name__ == "__main__":
    test_validate_binary_search_tree()
    test_performance()
