"""
LeetCode 153. Find Minimum in Rotated Sorted Array
Difficulty: Medium
Category: Binary Search

Suppose an array of length n sorted in ascending order is rotated between 1 and n times. 
For example, the array nums = [0,1,2,4,5,6,7] might become:
- [4,5,6,7,0,1,2] if it was rotated 4 times.
- [0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array 
[a[n-1], a[0], a[1], a[2], ..., a[n-2]].
Given the sorted rotated array nums of unique elements, return the minimum element of this array.

Time Complexity: O(log n)
Space Complexity: O(1)
"""

def findMin(nums):
    """
    Find minimum element in rotated sorted array.
    
    Args:
        nums: Rotated sorted array
        
    Returns:
        Minimum element in array
    """
    # TODO: Implement your solution here
    pass


# Test cases
def test_find_minimum_in_rotated_sorted_array():
    """Test cases for Find Minimum in Rotated Sorted Array"""
    test_cases = [
        # Basic test cases
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
        
        # Edge cases
        ([1], 1),
        ([1, 2], 1),
        ([2, 1], 1),
        ([1, 2, 3], 1),
        ([3, 1, 2], 1),
        ([2, 3, 1], 1),
        
        # LeetCode test cases
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
        
        # Additional test cases
        ([1, 2, 3, 4, 5], 1),
        ([2, 3, 4, 5, 1], 1),
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 1, 2, 3], 1),
        ([5, 1, 2, 3, 4], 1),
        
        # No rotation
        ([1, 2, 3, 4, 5], 1),
        ([1, 2, 3, 4, 5, 6], 1),
        ([1, 2, 3, 4, 5, 6, 7], 1),
        
        # Full rotation
        ([5, 1, 2, 3, 4], 1),
        ([6, 1, 2, 3, 4, 5], 1),
        ([7, 1, 2, 3, 4, 5, 6], 1),
        
        # Two elements
        ([1, 2], 1),
        ([2, 1], 1),
        
        # Three elements
        ([1, 2, 3], 1),
        ([3, 1, 2], 1),
        ([2, 3, 1], 1),
        
        # Four elements
        ([1, 2, 3, 4], 1),
        ([4, 1, 2, 3], 1),
        ([3, 4, 1, 2], 1),
        ([2, 3, 4, 1], 1),
        
        # Five elements
        ([1, 2, 3, 4, 5], 1),
        ([5, 1, 2, 3, 4], 1),
        ([4, 5, 1, 2, 3], 1),
        ([3, 4, 5, 1, 2], 1),
        ([2, 3, 4, 5, 1], 1),
        
        # Large arrays
        (list(range(1, 101)), 1),
        (list(range(51, 101)) + list(range(1, 51)), 1),
        (list(range(76, 101)) + list(range(1, 76)), 1),
        (list(range(90, 101)) + list(range(1, 90)), 1),
        (list(range(95, 101)) + list(range(1, 95)), 1),
        
        # Negative numbers
        ([-1, 0, 1, 2, 3], -1),
        ([2, 3, -1, 0, 1], -1),
        ([1, 2, 3, -1, 0], -1),
        ([0, 1, 2, 3, -1], -1),
        ([3, -1, 0, 1, 2], -1),
        
        # Mixed positive and negative
        ([-5, -4, -3, -2, -1], -5),
        ([-2, -1, -5, -4, -3], -5),
        ([-1, -5, -4, -3, -2], -5),
        ([-4, -3, -2, -1, -5], -5),
        ([-3, -2, -1, -5, -4], -5),
        
        # Duplicates
        ([1, 1, 1, 1], 1),
        ([1, 1, 2, 1], 1),
        ([2, 1, 1, 1], 1),
        ([1, 2, 1, 1], 1),
        ([1, 1, 1, 2], 1),
        
        # Edge cases with duplicates
        ([1, 1, 1, 1, 1], 1),
        ([1, 1, 1, 1, 2], 1),
        ([2, 1, 1, 1, 1], 1),
        ([1, 2, 1, 1, 1], 1),
        ([1, 1, 2, 1, 1], 1),
        ([1, 1, 1, 2, 1], 1),
        
        # Single element
        ([1], 1),
        ([0], 0),
        ([-1], -1),
        ([100], 100),
        ([-100], -100),
        
        # Two elements with duplicates
        ([1, 1], 1),
        ([2, 2], 2),
        ([0, 0], 0),
        ([-1, -1], -1),
        
        # Three elements with duplicates
        ([1, 1, 1], 1),
        ([1, 1, 2], 1),
        ([2, 1, 1], 1),
        ([1, 2, 1], 1),
        ([1, 1, 1, 1], 1),
        ([1, 1, 1, 2], 1),
        ([2, 1, 1, 1], 1),
        ([1, 2, 1, 1], 1),
        ([1, 1, 2, 1], 1),
        
        # Large numbers
        ([1000000000, 1000000001, 1000000002], 1000000000),
        ([1000000002, 1000000000, 1000000001], 1000000000),
        ([1000000001, 1000000002, 1000000000], 1000000000),
        
        # Very large numbers
        ([2147483647, 1, 2], 1),
        ([2, 2147483647, 1], 1),
        ([1, 2, 2147483647], 1),
        
        # Edge cases with rotation
        ([1, 2], 1),
        ([2, 1], 1),
        ([1, 2, 3], 1),
        ([3, 1, 2], 1),
        ([2, 3, 1], 1),
        ([1, 2, 3, 4], 1),
        ([4, 1, 2, 3], 1),
        ([3, 4, 1, 2], 1),
        ([2, 3, 4, 1], 1),
    ]
    
    print("Testing Find Minimum in Rotated Sorted Array solution...")
    for i, (nums, expected) in enumerate(test_cases):
        result = findMin(nums)
        if result == expected:
            print(f"✓ Test {i+1} passed: nums={nums}, result={result}")
        else:
            print(f"✗ Test {i+1} failed: nums={nums}")
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
    
    start_time = time.time()
    result = findMin(large_nums)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large array (10,000 elements): {end_time - start_time:.4f} seconds")
    print(f"Result: {result}")


if __name__ == "__main__":
    test_find_minimum_in_rotated_sorted_array()
    test_performance()
