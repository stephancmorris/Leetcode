"""
LeetCode 2. Add Two Numbers
Difficulty: Medium
Category: Linked List

You are given two non-empty linked lists representing two non-negative integers. The digits 
are stored in reverse order, and each of their nodes contains a single digit. Add the two 
numbers and return the sum as a linked list.

Time Complexity: O(max(m, n))
Space Complexity: O(max(m, n))
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    """
    Add two numbers represented as linked lists.
    
    Args:
        l1: First linked list representing a number
        l2: Second linked list representing a number
        
    Returns:
        Linked list representing the sum
    """
    # TODO: Implement your solution here
    pass


# Test cases
def test_add_two_numbers():
    """Test cases for Add Two Numbers"""
    test_cases = [
        # Basic test cases
        (create_list([2, 4, 3]), create_list([5, 6, 4]), [7, 0, 8]),
        (create_list([0]), create_list([0]), [0]),
        (create_list([9, 9, 9, 9, 9, 9, 9]), create_list([9, 9, 9, 9]), [8, 9, 9, 9, 0, 0, 0, 1]),
        
        # Edge cases
        (create_list([0]), create_list([0]), [0]),
        (create_list([1]), create_list([1]), [2]),
        (create_list([9]), create_list([1]), [0, 1]),
        (create_list([9, 9]), create_list([1]), [0, 0, 1]),
        (create_list([1]), create_list([9, 9]), [0, 0, 1]),
        
        # LeetCode test cases
        (create_list([2, 4, 3]), create_list([5, 6, 4]), [7, 0, 8]),
        (create_list([0]), create_list([0]), [0]),
        (create_list([9, 9, 9, 9, 9, 9, 9]), create_list([9, 9, 9, 9]), [8, 9, 9, 9, 0, 0, 0, 1]),
        
        # Additional test cases
        (create_list([1, 2, 3]), create_list([4, 5, 6]), [5, 7, 9]),
        (create_list([1, 2, 3]), create_list([4, 5, 6, 7]), [5, 7, 9, 7]),
        (create_list([1, 2, 3, 4]), create_list([5, 6, 7]), [6, 8, 0, 5]),
        (create_list([1, 2, 3, 4]), create_list([5, 6, 7, 8]), [6, 8, 0, 3, 1]),
        
        # Single digits
        (create_list([1]), create_list([2]), [3]),
        (create_list([5]), create_list([5]), [0, 1]),
        (create_list([9]), create_list([9]), [8, 1]),
        (create_list([0]), create_list([1]), [1]),
        (create_list([1]), create_list([0]), [1]),
        
        # Two digits
        (create_list([1, 2]), create_list([3, 4]), [4, 6]),
        (create_list([1, 2]), create_list([3, 4, 5]), [4, 6, 5]),
        (create_list([1, 2, 3]), create_list([4, 5]), [5, 7, 3]),
        (create_list([1, 2]), create_list([3, 4, 5, 6]), [4, 6, 5, 6]),
        (create_list([1, 2, 3, 4]), create_list([5, 6]), [6, 8, 3, 4]),
        
        # Three digits
        (create_list([1, 2, 3]), create_list([4, 5, 6]), [5, 7, 9]),
        (create_list([1, 2, 3]), create_list([4, 5, 6, 7]), [5, 7, 9, 7]),
        (create_list([1, 2, 3, 4]), create_list([5, 6, 7]), [6, 8, 0, 5]),
        (create_list([1, 2, 3, 4]), create_list([5, 6, 7, 8]), [6, 8, 0, 3, 1]),
        
        # Four digits
        (create_list([1, 2, 3, 4]), create_list([5, 6, 7, 8]), [6, 8, 0, 3, 1]),
        (create_list([1, 2, 3, 4]), create_list([5, 6, 7, 8, 9]), [6, 8, 0, 3, 0, 1]),
        (create_list([1, 2, 3, 4, 5]), create_list([6, 7, 8, 9]), [7, 9, 1, 4, 6]),
        (create_list([1, 2, 3, 4, 5]), create_list([6, 7, 8, 9, 0]), [7, 9, 1, 4, 6]),
        
        # Five digits
        (create_list([1, 2, 3, 4, 5]), create_list([6, 7, 8, 9, 0]), [7, 9, 1, 4, 6]),
        (create_list([1, 2, 3, 4, 5]), create_list([6, 7, 8, 9, 0, 1]), [7, 9, 1, 4, 6, 1]),
        (create_list([1, 2, 3, 4, 5, 6]), create_list([7, 8, 9, 0, 1]), [8, 0, 3, 5, 6, 6]),
        (create_list([1, 2, 3, 4, 5, 6]), create_list([7, 8, 9, 0, 1, 2]), [8, 0, 3, 5, 6, 8]),
        
        # Six digits
        (create_list([1, 2, 3, 4, 5, 6]), create_list([7, 8, 9, 0, 1, 2]), [8, 0, 3, 5, 6, 8]),
        (create_list([1, 2, 3, 4, 5, 6]), create_list([7, 8, 9, 0, 1, 2, 3]), [8, 0, 3, 5, 6, 8, 3]),
        (create_list([1, 2, 3, 4, 5, 6, 7]), create_list([8, 9, 0, 1, 2, 3]), [9, 1, 4, 6, 7, 9, 7]),
        (create_list([1, 2, 3, 4, 5, 6, 7]), create_list([8, 9, 0, 1, 2, 3, 4]), [9, 1, 4, 6, 7, 9, 1, 1]),
        
        # Seven digits
        (create_list([1, 2, 3, 4, 5, 6, 7]), create_list([8, 9, 0, 1, 2, 3, 4]), [9, 1, 4, 6, 7, 9, 1, 1]),
        (create_list([1, 2, 3, 4, 5, 6, 7]), create_list([8, 9, 0, 1, 2, 3, 4, 5]), [9, 1, 4, 6, 7, 9, 1, 6]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8]), create_list([9, 0, 1, 2, 3, 4, 5]), [0, 3, 5, 7, 8, 0, 3, 8]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8]), create_list([9, 0, 1, 2, 3, 4, 5, 6]), [0, 3, 5, 7, 8, 0, 3, 5, 1]),
        
        # Eight digits
        (create_list([1, 2, 3, 4, 5, 6, 7, 8]), create_list([9, 0, 1, 2, 3, 4, 5, 6]), [0, 3, 5, 7, 8, 0, 3, 5, 1]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8]), create_list([9, 0, 1, 2, 3, 4, 5, 6, 7]), [0, 3, 5, 7, 8, 0, 3, 5, 8]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9]), create_list([0, 1, 2, 3, 4, 5, 6, 7]), [1, 3, 5, 7, 9, 1, 4, 6, 9]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9]), create_list([0, 1, 2, 3, 4, 5, 6, 7, 8]), [1, 3, 5, 7, 9, 1, 4, 6, 8, 1]),
        
        # Nine digits
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9]), create_list([0, 1, 2, 3, 4, 5, 6, 7, 8]), [1, 3, 5, 7, 9, 1, 4, 6, 8, 1]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9]), create_list([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]), [1, 3, 5, 7, 9, 1, 4, 6, 8, 0, 1]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), create_list([1, 2, 3, 4, 5, 6, 7, 8, 9]), [2, 4, 6, 8, 0, 3, 5, 7, 9, 0]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), create_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), [2, 4, 6, 8, 0, 3, 5, 7, 9, 0]),
        
        # Ten digits
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), create_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), [2, 4, 6, 8, 0, 3, 5, 7, 9, 0]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), create_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]), [2, 4, 6, 8, 0, 3, 5, 7, 9, 0, 1]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]), create_list([2, 3, 4, 5, 6, 7, 8, 9, 0, 1]), [3, 5, 7, 9, 1, 4, 6, 8, 0, 2]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 1]), create_list([2, 3, 4, 5, 6, 7, 8, 9, 0, 1, 2]), [3, 5, 7, 9, 1, 4, 6, 8, 0, 2, 3]),
        
        # Large numbers
        (create_list([9] * 100), create_list([1]), [0] * 100 + [1]),
        (create_list([1]), create_list([9] * 100), [0] * 100 + [1]),
        (create_list([9] * 100), create_list([9] * 100), [8] * 100 + [1]),
        
        # Very large numbers
        (create_list([9] * 1000), create_list([1]), [0] * 1000 + [1]),
        (create_list([1]), create_list([9] * 1000), [0] * 1000 + [1]),
        (create_list([9] * 1000), create_list([9] * 1000), [8] * 1000 + [1]),
        
        # Edge cases with zeros
        (create_list([0]), create_list([0]), [0]),
        (create_list([0]), create_list([1]), [1]),
        (create_list([1]), create_list([0]), [1]),
        (create_list([0, 0]), create_list([0, 0]), [0, 0]),
        (create_list([0, 0]), create_list([1, 1]), [1, 1]),
        (create_list([1, 1]), create_list([0, 0]), [1, 1]),
        
        # Edge cases with ones
        (create_list([1]), create_list([1]), [2]),
        (create_list([1, 1]), create_list([1, 1]), [2, 2]),
        (create_list([1, 1, 1]), create_list([1, 1, 1]), [2, 2, 2]),
        (create_list([1, 1, 1, 1]), create_list([1, 1, 1, 1]), [2, 2, 2, 2]),
        
        # Edge cases with nines
        (create_list([9]), create_list([9]), [8, 1]),
        (create_list([9, 9]), create_list([9, 9]), [8, 9, 1]),
        (create_list([9, 9, 9]), create_list([9, 9, 9]), [8, 9, 9, 1]),
        (create_list([9, 9, 9, 9]), create_list([9, 9, 9, 9]), [8, 9, 9, 9, 1]),
        
        # Mixed lengths
        (create_list([1]), create_list([9, 9, 9]), [0, 0, 0, 1]),
        (create_list([9, 9, 9]), create_list([1]), [0, 0, 0, 1]),
        (create_list([1, 2]), create_list([9, 9, 9]), [0, 2, 9, 1]),
        (create_list([9, 9, 9]), create_list([1, 2]), [0, 2, 9, 1]),
        (create_list([1, 2, 3]), create_list([9, 9, 9]), [0, 2, 3, 1]),
        (create_list([9, 9, 9]), create_list([1, 2, 3]), [0, 2, 3, 1]),
    ]
    
    print("Testing Add Two Numbers solution...")
    for i, (l1, l2, expected) in enumerate(test_cases):
        result = addTwoNumbers(l1, l2)
        result_list = list_to_array(result)
        
        if result_list == expected:
            print(f"✓ Test {i+1} passed: l1={list_to_array(l1)}, l2={list_to_array(l2)}, result={result_list}")
        else:
            print(f"✗ Test {i+1} failed: l1={list_to_array(l1)}, l2={list_to_array(l2)}")
            print(f"  Expected: {expected}, Got: {result_list}")
    
    print("\nAll tests completed!")


def create_list(values):
    """Create a linked list from a list of values"""
    if not values:
        return None
    
    head = ListNode(values[0])
    current = head
    
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head


def list_to_array(head):
    """Convert a linked list to an array"""
    result = []
    current = head
    
    while current:
        result.append(current.val)
        current = current.next
    
    return result


# Performance test
def test_performance():
    """Test solution performance with large input"""
    import time
    
    # Generate large linked lists
    large_l1 = create_list([9] * 1000)
    large_l2 = create_list([9] * 1000)
    
    start_time = time.time()
    result = addTwoNumbers(large_l1, large_l2)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large linked lists (1000 nodes each): {end_time - start_time:.4f} seconds")
    print(f"Result length: {len(list_to_array(result))}")


if __name__ == "__main__":
    test_add_two_numbers()
    test_performance()
