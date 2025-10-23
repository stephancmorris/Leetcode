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


# Test cases
def test_copy_list_with_random_pointer():
    """Test cases for Copy List with Random Pointer"""
    test_cases = [
        # Basic test cases
        (create_list_with_random([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]), [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]),
        (create_list_with_random([[1, 1], [2, 1]]), [[1, 1], [2, 1]]),
        (create_list_with_random([[3, None], [3, 0], [3, None]]), [[3, None], [3, 0], [3, None]]),
        
        # Edge cases
        (create_list_with_random([]), []),
        (create_list_with_random([[1, None]]), [[1, None]]),
        (create_list_with_random([[1, 0]]), [[1, 0]]),
        
        # LeetCode test cases
        (create_list_with_random([[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]), [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]),
        (create_list_with_random([[1, 1], [2, 1]]), [[1, 1], [2, 1]]),
        (create_list_with_random([[3, None], [3, 0], [3, None]]), [[3, None], [3, 0], [3, None]]),
        
        # Additional test cases
        (create_list_with_random([[1, None]]), [[1, None]]),
        (create_list_with_random([[1, 0]]), [[1, 0]]),
        (create_list_with_random([[1, 1]]), [[1, 1]]),
        (create_list_with_random([[1, None], [2, None]]), [[1, None], [2, None]]),
        (create_list_with_random([[1, 0], [2, 1]]), [[1, 0], [2, 1]]),
        (create_list_with_random([[1, 1], [2, 0]]), [[1, 1], [2, 0]]),
        (create_list_with_random([[1, 0], [2, 0]]), [[1, 0], [2, 0]]),
        (create_list_with_random([[1, 1], [2, 1]]), [[1, 1], [2, 1]]),
        
        # Three nodes
        (create_list_with_random([[1, None], [2, None], [3, None]]), [[1, None], [2, None], [3, None]]),
        (create_list_with_random([[1, 0], [2, 1], [3, 2]]), [[1, 0], [2, 1], [3, 2]]),
        (create_list_with_random([[1, 2], [2, 0], [3, 1]]), [[1, 2], [2, 0], [3, 1]]),
        (create_list_with_random([[1, 0], [2, 0], [3, 0]]), [[1, 0], [2, 0], [3, 0]]),
        (create_list_with_random([[1, 1], [2, 1], [3, 1]]), [[1, 1], [2, 1], [3, 1]]),
        (create_list_with_random([[1, 2], [2, 2], [3, 2]]), [[1, 2], [2, 2], [3, 2]]),
        
        # Four nodes
        (create_list_with_random([[1, None], [2, None], [3, None], [4, None]]), [[1, None], [2, None], [3, None], [4, None]]),
        (create_list_with_random([[1, 0], [2, 1], [3, 2], [4, 3]]), [[1, 0], [2, 1], [3, 2], [4, 3]]),
        (create_list_with_random([[1, 3], [2, 0], [3, 1], [4, 2]]), [[1, 3], [2, 0], [3, 1], [4, 2]]),
        (create_list_with_random([[1, 0], [2, 0], [3, 0], [4, 0]]), [[1, 0], [2, 0], [3, 0], [4, 0]]),
        (create_list_with_random([[1, 1], [2, 1], [3, 1], [4, 1]]), [[1, 1], [2, 1], [3, 1], [4, 1]]),
        (create_list_with_random([[1, 2], [2, 2], [3, 2], [4, 2]]), [[1, 2], [2, 2], [3, 2], [4, 2]]),
        (create_list_with_random([[1, 3], [2, 3], [3, 3], [4, 3]]), [[1, 3], [2, 3], [3, 3], [4, 3]]),
        
        # Five nodes
        (create_list_with_random([[1, None], [2, None], [3, None], [4, None], [5, None]]), [[1, None], [2, None], [3, None], [4, None], [5, None]]),
        (create_list_with_random([[1, 0], [2, 1], [3, 2], [4, 3], [5, 4]]), [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4]]),
        (create_list_with_random([[1, 4], [2, 0], [3, 1], [4, 2], [5, 3]]), [[1, 4], [2, 0], [3, 1], [4, 2], [5, 3]]),
        (create_list_with_random([[1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]), [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]),
        (create_list_with_random([[1, 1], [2, 1], [3, 1], [4, 1], [5, 1]]), [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1]]),
        (create_list_with_random([[1, 2], [2, 2], [3, 2], [4, 2], [5, 2]]), [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2]]),
        (create_list_with_random([[1, 3], [2, 3], [3, 3], [4, 3], [5, 3]]), [[1, 3], [2, 3], [3, 3], [4, 3], [5, 3]]),
        (create_list_with_random([[1, 4], [2, 4], [3, 4], [4, 4], [5, 4]]), [[1, 4], [2, 4], [3, 4], [4, 4], [5, 4]]),
        
        # Six nodes
        (create_list_with_random([[1, None], [2, None], [3, None], [4, None], [5, None], [6, None]]), [[1, None], [2, None], [3, None], [4, None], [5, None], [6, None]]),
        (create_list_with_random([[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5]]), [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5]]),
        (create_list_with_random([[1, 5], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4]]), [[1, 5], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4]]),
        (create_list_with_random([[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]]), [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0]]),
        (create_list_with_random([[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1]]), [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1]]),
        (create_list_with_random([[1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2]]), [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2]]),
        (create_list_with_random([[1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3]]), [[1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3]]),
        (create_list_with_random([[1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4]]), [[1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4]]),
        (create_list_with_random([[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5]]), [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5]]),
        
        # Seven nodes
        (create_list_with_random([[1, None], [2, None], [3, None], [4, None], [5, None], [6, None], [7, None]]), [[1, None], [2, None], [3, None], [4, None], [5, None], [6, None], [7, None]]),
        (create_list_with_random([[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6]]), [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6]]),
        (create_list_with_random([[1, 6], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5]]), [[1, 6], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5]]),
        (create_list_with_random([[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]]), [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0]]),
        (create_list_with_random([[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1]]), [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1]]),
        (create_list_with_random([[1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2]]), [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2]]),
        (create_list_with_random([[1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3]]), [[1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3]]),
        (create_list_with_random([[1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4]]), [[1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4]]),
        (create_list_with_random([[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5]]), [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5]]),
        (create_list_with_random([[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6], [7, 6]]), [[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6], [7, 6]]),
        
        # Eight nodes
        (create_list_with_random([[1, None], [2, None], [3, None], [4, None], [5, None], [6, None], [7, None], [8, None]]), [[1, None], [2, None], [3, None], [4, None], [5, None], [6, None], [7, None], [8, None]]),
        (create_list_with_random([[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7]]), [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7]]),
        (create_list_with_random([[1, 7], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5], [8, 6]]), [[1, 7], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5], [8, 6]]),
        (create_list_with_random([[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0]]), [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0]]),
        (create_list_with_random([[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1]]), [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1]]),
        (create_list_with_random([[1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2]]), [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2]]),
        (create_list_with_random([[1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3], [8, 3]]), [[1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3], [8, 3]]),
        (create_list_with_random([[1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [8, 4]]), [[1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [8, 4]]),
        (create_list_with_random([[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5]]), [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5]]),
        (create_list_with_random([[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6], [7, 6], [8, 6]]), [[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6], [7, 6], [8, 6]]),
        (create_list_with_random([[1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [7, 7], [8, 7]]), [[1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [7, 7], [8, 7]]),
        
        # Nine nodes
        (create_list_with_random([[1, None], [2, None], [3, None], [4, None], [5, None], [6, None], [7, None], [8, None], [9, None]]), [[1, None], [2, None], [3, None], [4, None], [5, None], [6, None], [7, None], [8, None], [9, None]]),
        (create_list_with_random([[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8]]), [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8]]),
        (create_list_with_random([[1, 8], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5], [8, 6], [9, 7]]), [[1, 8], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5], [8, 6], [9, 7]]),
        (create_list_with_random([[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]]), [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0]]),
        (create_list_with_random([[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]]), [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1]]),
        (create_list_with_random([[1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2]]), [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2]]),
        (create_list_with_random([[1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3], [8, 3], [9, 3]]), [[1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3], [8, 3], [9, 3]]),
        (create_list_with_random([[1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [8, 4], [9, 4]]), [[1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [8, 4], [9, 4]]),
        (create_list_with_random([[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5], [9, 5]]), [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5], [9, 5]]),
        (create_list_with_random([[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6], [7, 6], [8, 6], [9, 6]]), [[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6], [7, 6], [8, 6], [9, 6]]),
        (create_list_with_random([[1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [7, 7], [8, 7], [9, 7]]), [[1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [7, 7], [8, 7], [9, 7]]),
        (create_list_with_random([[1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [8, 8], [9, 8]]), [[1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [8, 8], [9, 8]]),
        
        # Ten nodes
        (create_list_with_random([[1, None], [2, None], [3, None], [4, None], [5, None], [6, None], [7, None], [8, None], [9, None], [0, None]]), [[1, None], [2, None], [3, None], [4, None], [5, None], [6, None], [7, None], [8, None], [9, None], [0, None]]),
        (create_list_with_random([[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [0, 9]]), [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4], [6, 5], [7, 6], [8, 7], [9, 8], [0, 9]]),
        (create_list_with_random([[1, 9], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5], [8, 6], [9, 7], [0, 8]]), [[1, 9], [2, 0], [3, 1], [4, 2], [5, 3], [6, 4], [7, 5], [8, 6], [9, 7], [0, 8]]),
        (create_list_with_random([[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [0, 0]]), [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0], [6, 0], [7, 0], [8, 0], [9, 0], [0, 0]]),
        (create_list_with_random([[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [0, 1]]), [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [0, 1]]),
        (create_list_with_random([[1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [0, 2]]), [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2], [6, 2], [7, 2], [8, 2], [9, 2], [0, 2]]),
        (create_list_with_random([[1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3], [8, 3], [9, 3], [0, 3]]), [[1, 3], [2, 3], [3, 3], [4, 3], [5, 3], [6, 3], [7, 3], [8, 3], [9, 3], [0, 3]]),
        (create_list_with_random([[1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [8, 4], [9, 4], [0, 4]]), [[1, 4], [2, 4], [3, 4], [4, 4], [5, 4], [6, 4], [7, 4], [8, 4], [9, 4], [0, 4]]),
        (create_list_with_random([[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5], [9, 5], [0, 5]]), [[1, 5], [2, 5], [3, 5], [4, 5], [5, 5], [6, 5], [7, 5], [8, 5], [9, 5], [0, 5]]),
        (create_list_with_random([[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6], [7, 6], [8, 6], [9, 6], [0, 6]]), [[1, 6], [2, 6], [3, 6], [4, 6], [5, 6], [6, 6], [7, 6], [8, 6], [9, 6], [0, 6]]),
        (create_list_with_random([[1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [7, 7], [8, 7], [9, 7], [0, 7]]), [[1, 7], [2, 7], [3, 7], [4, 7], [5, 7], [6, 7], [7, 7], [8, 7], [9, 7], [0, 7]]),
        (create_list_with_random([[1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [8, 8], [9, 8], [0, 8]]), [[1, 8], [2, 8], [3, 8], [4, 8], [5, 8], [6, 8], [7, 8], [8, 8], [9, 8], [0, 8]]),
        (create_list_with_random([[1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9], [9, 9], [0, 9]]), [[1, 9], [2, 9], [3, 9], [4, 9], [5, 9], [6, 9], [7, 9], [8, 9], [9, 9], [0, 9]]),
        
        # Large lists
        (create_list_with_random([[i, None] for i in range(1, 101)]), [[i, None] for i in range(1, 101)]),
        (create_list_with_random([[i, 0] for i in range(1, 101)]), [[i, 0] for i in range(1, 101)]),
        (create_list_with_random([[i, 1] for i in range(1, 101)]), [[i, 1] for i in range(1, 101)]),
        (create_list_with_random([[i, 2] for i in range(1, 101)]), [[i, 2] for i in range(1, 101)]),
        (create_list_with_random([[i, 3] for i in range(1, 101)]), [[i, 3] for i in range(1, 101)]),
        (create_list_with_random([[i, 4] for i in range(1, 101)]), [[i, 4] for i in range(1, 101)]),
        (create_list_with_random([[i, 5] for i in range(1, 101)]), [[i, 5] for i in range(1, 101)]),
        (create_list_with_random([[i, 6] for i in range(1, 101)]), [[i, 6] for i in range(1, 101)]),
        (create_list_with_random([[i, 7] for i in range(1, 101)]), [[i, 7] for i in range(1, 101)]),
        (create_list_with_random([[i, 8] for i in range(1, 101)]), [[i, 8] for i in range(1, 101)]),
        (create_list_with_random([[i, 9] for i in range(1, 101)]), [[i, 9] for i in range(1, 101)]),
        
        # Very large lists
        (create_list_with_random([[i, None] for i in range(1, 1001)]), [[i, None] for i in range(1, 1001)]),
        (create_list_with_random([[i, 0] for i in range(1, 1001)]), [[i, 0] for i in range(1, 1001)]),
        (create_list_with_random([[i, 1] for i in range(1, 1001)]), [[i, 1] for i in range(1, 1001)]),
        (create_list_with_random([[i, 2] for i in range(1, 1001)]), [[i, 2] for i in range(1, 1001)]),
        (create_list_with_random([[i, 3] for i in range(1, 1001)]), [[i, 3] for i in range(1, 1001)]),
        (create_list_with_random([[i, 4] for i in range(1, 1001)]), [[i, 4] for i in range(1, 1001)]),
        (create_list_with_random([[i, 5] for i in range(1, 1001)]), [[i, 5] for i in range(1, 1001)]),
        (create_list_with_random([[i, 6] for i in range(1, 1001)]), [[i, 6] for i in range(1, 1001)]),
        (create_list_with_random([[i, 7] for i in range(1, 1001)]), [[i, 7] for i in range(1, 1001)]),
        (create_list_with_random([[i, 8] for i in range(1, 1001)]), [[i, 8] for i in range(1, 1001)]),
        (create_list_with_random([[i, 9] for i in range(1, 1001)]), [[i, 9] for i in range(1, 1001)]),
        
        # Edge cases with empty list
        (create_list_with_random([]), []),
        
        # Edge cases with single node
        (create_list_with_random([[1, None]]), [[1, None]]),
        (create_list_with_random([[1, 0]]), [[1, 0]]),
        (create_list_with_random([[1, 1]]), [[1, 1]]),
        
        # Edge cases with two nodes
        (create_list_with_random([[1, None], [2, None]]), [[1, None], [2, None]]),
        (create_list_with_random([[1, 0], [2, 1]]), [[1, 0], [2, 1]]),
        (create_list_with_random([[1, 1], [2, 0]]), [[1, 1], [2, 0]]),
        (create_list_with_random([[1, 0], [2, 0]]), [[1, 0], [2, 0]]),
        (create_list_with_random([[1, 1], [2, 1]]), [[1, 1], [2, 1]]),
        
        # Edge cases with three nodes
        (create_list_with_random([[1, None], [2, None], [3, None]]), [[1, None], [2, None], [3, None]]),
        (create_list_with_random([[1, 0], [2, 1], [3, 2]]), [[1, 0], [2, 1], [3, 2]]),
        (create_list_with_random([[1, 2], [2, 0], [3, 1]]), [[1, 2], [2, 0], [3, 1]]),
        (create_list_with_random([[1, 0], [2, 0], [3, 0]]), [[1, 0], [2, 0], [3, 0]]),
        (create_list_with_random([[1, 1], [2, 1], [3, 1]]), [[1, 1], [2, 1], [3, 1]]),
        (create_list_with_random([[1, 2], [2, 2], [3, 2]]), [[1, 2], [2, 2], [3, 2]]),
        
        # Edge cases with four nodes
        (create_list_with_random([[1, None], [2, None], [3, None], [4, None]]), [[1, None], [2, None], [3, None], [4, None]]),
        (create_list_with_random([[1, 0], [2, 1], [3, 2], [4, 3]]), [[1, 0], [2, 1], [3, 2], [4, 3]]),
        (create_list_with_random([[1, 3], [2, 0], [3, 1], [4, 2]]), [[1, 3], [2, 0], [3, 1], [4, 2]]),
        (create_list_with_random([[1, 0], [2, 0], [3, 0], [4, 0]]), [[1, 0], [2, 0], [3, 0], [4, 0]]),
        (create_list_with_random([[1, 1], [2, 1], [3, 1], [4, 1]]), [[1, 1], [2, 1], [3, 1], [4, 1]]),
        (create_list_with_random([[1, 2], [2, 2], [3, 2], [4, 2]]), [[1, 2], [2, 2], [3, 2], [4, 2]]),
        (create_list_with_random([[1, 3], [2, 3], [3, 3], [4, 3]]), [[1, 3], [2, 3], [3, 3], [4, 3]]),
        
        # Edge cases with five nodes
        (create_list_with_random([[1, None], [2, None], [3, None], [4, None], [5, None]]), [[1, None], [2, None], [3, None], [4, None], [5, None]]),
        (create_list_with_random([[1, 0], [2, 1], [3, 2], [4, 3], [5, 4]]), [[1, 0], [2, 1], [3, 2], [4, 3], [5, 4]]),
        (create_list_with_random([[1, 4], [2, 0], [3, 1], [4, 2], [5, 3]]), [[1, 4], [2, 0], [3, 1], [4, 2], [5, 3]]),
        (create_list_with_random([[1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]), [[1, 0], [2, 0], [3, 0], [4, 0], [5, 0]]),
        (create_list_with_random([[1, 1], [2, 1], [3, 1], [4, 1], [5, 1]]), [[1, 1], [2, 1], [3, 1], [4, 1], [5, 1]]),
        (create_list_with_random([[1, 2], [2, 2], [3, 2], [4, 2], [5, 2]]), [[1, 2], [2, 2], [3, 2], [4, 2], [5, 2]]),
        (create_list_with_random([[1, 3], [2, 3], [3, 3], [4, 3], [5, 3]]), [[1, 3], [2, 3], [3, 3], [4, 3], [5, 3]]),
        (create_list_with_random([[1, 4], [2, 4], [3, 4], [4, 4], [5, 4]]), [[1, 4], [2, 4], [3, 4], [4, 4], [5, 4]]),
    ]
    
    print("Testing Copy List with Random Pointer solution...")
    for i, (head, expected) in enumerate(test_cases):
        result = copyRandomList(head)
        result_list = list_to_array_with_random(result)
        
        if result_list == expected:
            print(f"✓ Test {i+1} passed: head={list_to_array_with_random(head)}, result={result_list}")
        else:
            print(f"✗ Test {i+1} failed: head={list_to_array_with_random(head)}")
            print(f"  Expected: {expected}, Got: {result_list}")
    
    print("\nAll tests completed!")


def create_list_with_random(values):
    """Create a linked list with random pointers from a list of [val, random_index] pairs"""
    if not values:
        return None
    
    # Create nodes
    nodes = []
    for val, _ in values:
        nodes.append(Node(val))
    
    # Set next pointers
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    # Set random pointers
    for i, (_, random_idx) in enumerate(values):
        if random_idx is not None:
            nodes[i].random = nodes[random_idx]
    
    return nodes[0] if nodes else None


def list_to_array_with_random(head):
    """Convert a linked list with random pointers to an array of [val, random_index] pairs"""
    if not head:
        return []
    
    # Create a list of nodes
    nodes = []
    current = head
    while current:
        nodes.append(current)
        current = current.next
    
    # Create result array
    result = []
    for node in nodes:
        val = node.val
        random_idx = None
        if node.random:
            random_idx = nodes.index(node.random)
        result.append([val, random_idx])
    
    return result


# Performance test
def test_performance():
    """Test solution performance with large input"""
    import time
    
    # Generate large linked list with random pointers
    large_list = create_list_with_random([[i, i % 10] for i in range(1, 10001)])
    
    start_time = time.time()
    result = copyRandomList(large_list)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large linked list (10,000 nodes): {end_time - start_time:.4f} seconds")
    print(f"Result length: {len(list_to_array_with_random(result))}")


if __name__ == "__main__":
    test_copy_list_with_random_pointer()
    test_performance()
