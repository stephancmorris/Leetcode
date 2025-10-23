"""
LeetCode 33. Search in Rotated Sorted Array
Difficulty: Medium
Category: Binary Search

There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k 
(1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], 
nums[0], nums[1], ..., nums[k-1]] (0-indexed).
Given the array nums after the possible rotation and an integer target, return the index of 
target if it is in nums, or -1 if it is not in nums.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def search(nums, target):
    """
    Search for target in rotated sorted array.
    
    Args:
        nums: Rotated sorted array
        target: Value to search for
        
    Returns:
        Index of target if found, -1 otherwise
    """
    # TODO: Implement your solution here
    pass


# Test cases
def test_search_in_rotated_sorted_array():
    """Test cases for Search in Rotated Sorted Array"""
    test_cases = [
        # Basic test cases
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        ([1], 1, 0),
        
        # Edge cases
        ([1], 0, -1),
        ([1], 1, 0),
        ([1, 3], 0, -1),
        ([1, 3], 1, 0),
        ([1, 3], 3, 1),
        ([1, 3], 2, -1),
        ([3, 1], 0, -1),
        ([3, 1], 1, 1),
        ([3, 1], 3, 0),
        ([3, 1], 2, -1),
        
        # LeetCode test cases
        ([4, 5, 6, 7, 0, 1, 2], 0, 4),
        ([4, 5, 6, 7, 0, 1, 2], 3, -1),
        ([1], 0, -1),
        
        # Additional test cases
        ([4, 5, 6, 7, 0, 1, 2], 4, 0),
        ([4, 5, 6, 7, 0, 1, 2], 5, 1),
        ([4, 5, 6, 7, 0, 1, 2], 6, 2),
        ([4, 5, 6, 7, 0, 1, 2], 7, 3),
        ([4, 5, 6, 7, 0, 1, 2], 1, 5),
        ([4, 5, 6, 7, 0, 1, 2], 2, 6),
        ([4, 5, 6, 7, 0, 1, 2], 8, -1),
        ([4, 5, 6, 7, 0, 1, 2], -1, -1),
        
        # No rotation
        ([1, 2, 3, 4, 5], 1, 0),
        ([1, 2, 3, 4, 5], 2, 1),
        ([1, 2, 3, 4, 5], 3, 2),
        ([1, 2, 3, 4, 5], 4, 3),
        ([1, 2, 3, 4, 5], 5, 4),
        ([1, 2, 3, 4, 5], 0, -1),
        ([1, 2, 3, 4, 5], 6, -1),
        
        # Full rotation
        ([5, 1, 2, 3, 4], 1, 1),
        ([5, 1, 2, 3, 4], 2, 2),
        ([5, 1, 2, 3, 4], 3, 3),
        ([5, 1, 2, 3, 4], 4, 4),
        ([5, 1, 2, 3, 4], 5, 0),
        ([5, 1, 2, 3, 4], 0, -1),
        ([5, 1, 2, 3, 4], 6, -1),
        
        # Two elements
        ([1, 2], 1, 0),
        ([1, 2], 2, 1),
        ([1, 2], 0, -1),
        ([1, 2], 3, -1),
        ([2, 1], 1, 1),
        ([2, 1], 2, 0),
        ([2, 1], 0, -1),
        ([2, 1], 3, -1),
        
        # Three elements
        ([1, 2, 3], 1, 0),
        ([1, 2, 3], 2, 1),
        ([1, 2, 3], 3, 2),
        ([1, 2, 3], 0, -1),
        ([1, 2, 3], 4, -1),
        ([3, 1, 2], 1, 1),
        ([3, 1, 2], 2, 2),
        ([3, 1, 2], 3, 0),
        ([3, 1, 2], 0, -1),
        ([3, 1, 2], 4, -1),
        ([2, 3, 1], 1, 2),
        ([2, 3, 1], 2, 0),
        ([2, 3, 1], 3, 1),
        ([2, 3, 1], 0, -1),
        ([2, 3, 1], 4, -1),
        
        # Four elements
        ([1, 2, 3, 4], 1, 0),
        ([1, 2, 3, 4], 2, 1),
        ([1, 2, 3, 4], 3, 2),
        ([1, 2, 3, 4], 4, 3),
        ([1, 2, 3, 4], 0, -1),
        ([1, 2, 3, 4], 5, -1),
        ([4, 1, 2, 3], 1, 1),
        ([4, 1, 2, 3], 2, 2),
        ([4, 1, 2, 3], 3, 3),
        ([4, 1, 2, 3], 4, 0),
        ([4, 1, 2, 3], 0, -1),
        ([4, 1, 2, 3], 5, -1),
        ([3, 4, 1, 2], 1, 2),
        ([3, 4, 1, 2], 2, 3),
        ([3, 4, 1, 2], 3, 0),
        ([3, 4, 1, 2], 4, 1),
        ([3, 4, 1, 2], 0, -1),
        ([3, 4, 1, 2], 5, -1),
        ([2, 3, 4, 1], 1, 3),
        ([2, 3, 4, 1], 2, 0),
        ([2, 3, 4, 1], 3, 1),
        ([2, 3, 4, 1], 4, 2),
        ([2, 3, 4, 1], 0, -1),
        ([2, 3, 4, 1], 5, -1),
        
        # Large arrays
        (list(range(1, 101)), 1, 0),
        (list(range(1, 101)), 50, 49),
        (list(range(1, 101)), 100, 99),
        (list(range(1, 101)), 0, -1),
        (list(range(1, 101)), 101, -1),
        
        # Rotated large arrays
        (list(range(51, 101)) + list(range(1, 51)), 1, 50),
        (list(range(51, 101)) + list(range(1, 51)), 50, 49),
        (list(range(51, 101)) + list(range(1, 51)), 51, 0),
        (list(range(51, 101)) + list(range(1, 51)), 100, 49),
        (list(range(51, 101)) + list(range(1, 51)), 0, -1),
        (list(range(51, 101)) + list(range(1, 51)), 101, -1),
        
        # Negative numbers
        ([-1, 0, 1, 2, 3], -1, 0),
        ([-1, 0, 1, 2, 3], 0, 1),
        ([-1, 0, 1, 2, 3], 1, 2),
        ([-1, 0, 1, 2, 3], 2, 3),
        ([-1, 0, 1, 2, 3], 3, 4),
        ([-1, 0, 1, 2, 3], -2, -1),
        ([-1, 0, 1, 2, 3], 4, -1),
        
        # Rotated negative numbers
        ([2, 3, -1, 0, 1], -1, 2),
        ([2, 3, -1, 0, 1], 0, 3),
        ([2, 3, -1, 0, 1], 1, 4),
        ([2, 3, -1, 0, 1], 2, 0),
        ([2, 3, -1, 0, 1], 3, 1),
        ([2, 3, -1, 0, 1], -2, -1),
        ([2, 3, -1, 0, 1], 4, -1),
        
        # Duplicates
        ([1, 1, 1, 1], 1, 0),
        ([1, 1, 1, 1], 0, -1),
        ([1, 1, 1, 1], 2, -1),
        ([1, 1, 2, 1], 1, 0),
        ([1, 1, 2, 1], 2, 2),
        ([1, 1, 2, 1], 0, -1),
        ([1, 1, 2, 1], 3, -1),
        
        # Edge cases with rotation
        ([1, 3], 1, 0),
        ([1, 3], 3, 1),
        ([1, 3], 0, -1),
        ([1, 3], 2, -1),
        ([1, 3], 4, -1),
        ([3, 1], 1, 1),
        ([3, 1], 3, 0),
        ([3, 1], 0, -1),
        ([3, 1], 2, -1),
        ([3, 1], 4, -1),
    ]
    
    print("Testing Search in Rotated Sorted Array solution...")
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
    import random
    
    # Generate large rotated array
    large_nums = list(range(1, 10001))
    # Rotate the array
    rotation_point = random.randint(1, 9999)
    large_nums = large_nums[rotation_point:] + large_nums[:rotation_point]
    target = random.randint(1, 10000)
    
    start_time = time.time()
    result = search(large_nums, target)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large array (10,000 elements): {end_time - start_time:.4f} seconds")
    print(f"Target: {target}, Result: {result}")


if __name__ == "__main__":
    test_search_in_rotated_sorted_array()
    test_performance()
