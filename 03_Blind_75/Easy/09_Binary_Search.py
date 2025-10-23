"""
LeetCode 704. Binary Search
Difficulty: Easy
Category: Binary Search

Given an array of integers nums which is sorted in ascending order, and an integer target, 
write a function to search target in nums. If target exists, then return its index. 
Otherwise, return -1.
You must write an algorithm with O(log n) runtime complexity.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def search(nums, target):
    """
    Search for target in sorted array using binary search.
    
    Args:
        nums: Sorted array of integers
        target: Target value to search for
        
    Returns:
        Index of target if found, -1 otherwise
    """
    # TODO: Implement your solution here
    pass


# Test cases
def test_binary_search():
    """Test cases for Binary Search"""
    test_cases = [
        # Basic test cases
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        
        # Edge cases
        ([1], 1, 0),
        ([1], 2, -1),
        ([], 1, -1),
        ([1, 2], 1, 0),
        ([1, 2], 2, 1),
        ([1, 2], 3, -1),
        
        # LeetCode test cases
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
        
        # Additional test cases
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 5, 4),
        ([1, 2, 3, 4, 5], 6, -1),
        ([1, 2, 3, 4, 5], 0, -1),
        
        # Negative numbers
        ([-5, -4, -3, -2, -1], -3, 2),
        ([-5, -4, -3, -2, -1], -5, 0),
        ([-5, -4, -3, -2, -1], -1, 4),
        ([-5, -4, -3, -2, -1], -6, -1),
        ([-5, -4, -3, -2, -1], 0, -1),
        
        # Large numbers
        ([1000000000, 2000000000, 3000000000], 2000000000, 1),
        ([1000000000, 2000000000, 3000000000], 1000000000, 0),
        ([1000000000, 2000000000, 3000000000], 3000000000, 2),
        
        # Duplicates
        ([1, 1, 2, 2, 3, 3], 2, 2),  # Should find any occurrence
        ([1, 1, 2, 2, 3, 3], 1, 0),  # Should find any occurrence
        ([1, 1, 2, 2, 3, 3], 3, 4),  # Should find any occurrence
        ([1, 1, 2, 2, 3, 3], 4, -1),
        
        # Single element
        ([42], 42, 0),
        ([42], 43, -1),
        ([42], 41, -1),
        
        # Two elements
        ([1, 3], 1, 0),
        ([1, 3], 3, 1),
        ([1, 3], 2, -1),
    ]
    
    print("Testing Binary Search solution...")
    for i, (nums, target, expected) in enumerate(test_cases):
        result = search(nums, target)
        if result == expected:
            print(f"✓ Test {i+1} passed: nums={nums}, target={target}, result={result}")
        else:
            print(f"✗ Test {i+1} failed: nums={nums}, target={target}")
            print(f"  Expected: {expected}, Got: {result}")
    
    print("\nAll tests completed!")


# Performance test
def test_performance():
    """Test solution performance with large input"""
    import time
    
    # Generate large sorted array
    large_nums = list(range(1, 100001))  # [1, 2, 3, ..., 100000]
    target = 50000  # Middle element
    
    start_time = time.time()
    result = search(large_nums, target)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large sorted array (100,000 elements): {end_time - start_time:.4f} seconds")
    print(f"Result: {result}")


if __name__ == "__main__":
    test_binary_search()
    test_performance()
