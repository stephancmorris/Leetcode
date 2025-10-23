"""
LeetCode 19. Remove Nth Node From End of List
Difficulty: Medium
Category: Linked List

Given the head of a linked list, remove the nth node from the end of the list and return its head.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    """
    Remove nth node from end of linked list.
    
    Args:
        head: Head of linked list
        n: Position from end to remove
        
    Returns:
        Head of modified linked list
    """
    # TODO: Implement your solution here
    pass


# Test cases
def test_remove_nth_node_from_end():
    """Test cases for Remove Nth Node From End"""
    test_cases = [
        # Basic test cases
        (create_list([1, 2, 3, 4, 5]), 2, [1, 2, 3, 5]),
        (create_list([1]), 1, []),
        (create_list([1, 2]), 1, [1]),
        (create_list([1, 2]), 2, [2]),
        
        # Edge cases
        (create_list([1]), 1, []),
        (create_list([1, 2]), 1, [1]),
        (create_list([1, 2]), 2, [2]),
        (create_list([1, 2, 3]), 1, [1, 2]),
        (create_list([1, 2, 3]), 2, [1, 3]),
        (create_list([1, 2, 3]), 3, [2, 3]),
        
        # LeetCode test cases
        (create_list([1, 2, 3, 4, 5]), 2, [1, 2, 3, 5]),
        (create_list([1]), 1, []),
        (create_list([1, 2]), 1, [1]),
        
        # Additional test cases
        (create_list([1, 2, 3, 4, 5]), 1, [1, 2, 3, 4]),
        (create_list([1, 2, 3, 4, 5]), 3, [1, 2, 4, 5]),
        (create_list([1, 2, 3, 4, 5]), 4, [1, 3, 4, 5]),
        (create_list([1, 2, 3, 4, 5]), 5, [2, 3, 4, 5]),
        
        # Single node
        (create_list([1]), 1, []),
        
        # Two nodes
        (create_list([1, 2]), 1, [1]),
        (create_list([1, 2]), 2, [2]),
        
        # Three nodes
        (create_list([1, 2, 3]), 1, [1, 2]),
        (create_list([1, 2, 3]), 2, [1, 3]),
        (create_list([1, 2, 3]), 3, [2, 3]),
        
        # Four nodes
        (create_list([1, 2, 3, 4]), 1, [1, 2, 3]),
        (create_list([1, 2, 3, 4]), 2, [1, 2, 4]),
        (create_list([1, 2, 3, 4]), 3, [1, 3, 4]),
        (create_list([1, 2, 3, 4]), 4, [2, 3, 4]),
        
        # Five nodes
        (create_list([1, 2, 3, 4, 5]), 1, [1, 2, 3, 4]),
        (create_list([1, 2, 3, 4, 5]), 2, [1, 2, 3, 5]),
        (create_list([1, 2, 3, 4, 5]), 3, [1, 2, 4, 5]),
        (create_list([1, 2, 3, 4, 5]), 4, [1, 3, 4, 5]),
        (create_list([1, 2, 3, 4, 5]), 5, [2, 3, 4, 5]),
        
        # Six nodes
        (create_list([1, 2, 3, 4, 5, 6]), 1, [1, 2, 3, 4, 5]),
        (create_list([1, 2, 3, 4, 5, 6]), 2, [1, 2, 3, 4, 6]),
        (create_list([1, 2, 3, 4, 5, 6]), 3, [1, 2, 3, 5, 6]),
        (create_list([1, 2, 3, 4, 5, 6]), 4, [1, 2, 4, 5, 6]),
        (create_list([1, 2, 3, 4, 5, 6]), 5, [1, 3, 4, 5, 6]),
        (create_list([1, 2, 3, 4, 5, 6]), 6, [2, 3, 4, 5, 6]),
        
        # Seven nodes
        (create_list([1, 2, 3, 4, 5, 6, 7]), 1, [1, 2, 3, 4, 5, 6]),
        (create_list([1, 2, 3, 4, 5, 6, 7]), 2, [1, 2, 3, 4, 5, 7]),
        (create_list([1, 2, 3, 4, 5, 6, 7]), 3, [1, 2, 3, 4, 6, 7]),
        (create_list([1, 2, 3, 4, 5, 6, 7]), 4, [1, 2, 3, 5, 6, 7]),
        (create_list([1, 2, 3, 4, 5, 6, 7]), 5, [1, 2, 4, 5, 6, 7]),
        (create_list([1, 2, 3, 4, 5, 6, 7]), 6, [1, 3, 4, 5, 6, 7]),
        (create_list([1, 2, 3, 4, 5, 6, 7]), 7, [2, 3, 4, 5, 6, 7]),
        
        # Eight nodes
        (create_list([1, 2, 3, 4, 5, 6, 7, 8]), 1, [1, 2, 3, 4, 5, 6, 7]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8]), 2, [1, 2, 3, 4, 5, 6, 8]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8]), 3, [1, 2, 3, 4, 5, 7, 8]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8]), 4, [1, 2, 3, 4, 6, 7, 8]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8]), 5, [1, 2, 3, 5, 6, 7, 8]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8]), 6, [1, 2, 4, 5, 6, 7, 8]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8]), 7, [1, 3, 4, 5, 6, 7, 8]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8]), 8, [2, 3, 4, 5, 6, 7, 8]),
        
        # Nine nodes
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9]), 1, [1, 2, 3, 4, 5, 6, 7, 8]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9]), 2, [1, 2, 3, 4, 5, 6, 7, 9]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9]), 3, [1, 2, 3, 4, 5, 6, 8, 9]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9]), 4, [1, 2, 3, 4, 5, 7, 8, 9]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9]), 5, [1, 2, 3, 4, 6, 7, 8, 9]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9]), 6, [1, 2, 3, 5, 6, 7, 8, 9]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9]), 7, [1, 2, 4, 5, 6, 7, 8, 9]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9]), 8, [1, 3, 4, 5, 6, 7, 8, 9]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9]), 9, [2, 3, 4, 5, 6, 7, 8, 9]),
        
        # Ten nodes
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), 1, [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), 2, [1, 2, 3, 4, 5, 6, 7, 8, 0]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), 3, [1, 2, 3, 4, 5, 6, 7, 9, 0]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), 4, [1, 2, 3, 4, 5, 6, 8, 9, 0]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), 5, [1, 2, 3, 4, 5, 7, 8, 9, 0]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), 6, [1, 2, 3, 4, 6, 7, 8, 9, 0]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), 7, [1, 2, 3, 5, 6, 7, 8, 9, 0]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), 8, [1, 2, 4, 5, 6, 7, 8, 9, 0]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), 9, [1, 3, 4, 5, 6, 7, 8, 9, 0]),
        (create_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), 10, [2, 3, 4, 5, 6, 7, 8, 9, 0]),
        
        # Large lists
        (create_list(list(range(1, 101))), 1, list(range(1, 100))),
        (create_list(list(range(1, 101))), 2, list(range(1, 99)) + [100]),
        (create_list(list(range(1, 101))), 50, list(range(1, 51)) + list(range(52, 101))),
        (create_list(list(range(1, 101))), 99, list(range(2, 101))),
        (create_list(list(range(1, 101))), 100, list(range(2, 101))),
        
        # Very large lists
        (create_list(list(range(1, 1001))), 1, list(range(1, 1000))),
        (create_list(list(range(1, 1001))), 2, list(range(1, 999)) + [1000]),
        (create_list(list(range(1, 1001))), 500, list(range(1, 501)) + list(range(502, 1001))),
        (create_list(list(range(1, 1001))), 999, list(range(2, 1001))),
        (create_list(list(range(1, 1001))), 1000, list(range(2, 1001))),
        
        # Edge cases with n
        (create_list([1, 2, 3, 4, 5]), 1, [1, 2, 3, 4]),
        (create_list([1, 2, 3, 4, 5]), 2, [1, 2, 3, 5]),
        (create_list([1, 2, 3, 4, 5]), 3, [1, 2, 4, 5]),
        (create_list([1, 2, 3, 4, 5]), 4, [1, 3, 4, 5]),
        (create_list([1, 2, 3, 4, 5]), 5, [2, 3, 4, 5]),
        
        # Edge cases with single node
        (create_list([1]), 1, []),
        
        # Edge cases with two nodes
        (create_list([1, 2]), 1, [1]),
        (create_list([1, 2]), 2, [2]),
        
        # Edge cases with three nodes
        (create_list([1, 2, 3]), 1, [1, 2]),
        (create_list([1, 2, 3]), 2, [1, 3]),
        (create_list([1, 2, 3]), 3, [2, 3]),
        
        # Edge cases with four nodes
        (create_list([1, 2, 3, 4]), 1, [1, 2, 3]),
        (create_list([1, 2, 3, 4]), 2, [1, 2, 4]),
        (create_list([1, 2, 3, 4]), 3, [1, 3, 4]),
        (create_list([1, 2, 3, 4]), 4, [2, 3, 4]),
        
        # Edge cases with five nodes
        (create_list([1, 2, 3, 4, 5]), 1, [1, 2, 3, 4]),
        (create_list([1, 2, 3, 4, 5]), 2, [1, 2, 3, 5]),
        (create_list([1, 2, 3, 4, 5]), 3, [1, 2, 4, 5]),
        (create_list([1, 2, 3, 4, 5]), 4, [1, 3, 4, 5]),
        (create_list([1, 2, 3, 4, 5]), 5, [2, 3, 4, 5]),
    ]
    
    print("Testing Remove Nth Node From End solution...")
    for i, (head, n, expected) in enumerate(test_cases):
        result = removeNthFromEnd(head, n)
        result_list = list_to_array(result)
        
        if result_list == expected:
            print(f"✓ Test {i+1} passed: head={list_to_array(head)}, n={n}, result={result_list}")
        else:
            print(f"✗ Test {i+1} failed: head={list_to_array(head)}, n={n}")
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
    
    # Generate large linked list
    large_list = create_list(list(range(1, 10001)))
    n = 5000
    
    start_time = time.time()
    result = removeNthFromEnd(large_list, n)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large linked list (10,000 nodes), remove {n}th from end: {end_time - start_time:.4f} seconds")
    print(f"Result length: {len(list_to_array(result))}")


if __name__ == "__main__":
    test_remove_nth_node_from_end()
    test_performance()
