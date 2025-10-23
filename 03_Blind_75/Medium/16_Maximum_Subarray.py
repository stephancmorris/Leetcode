"""
LeetCode 53. Maximum Subarray
Difficulty: Medium
Category: Arrays & Hashing

Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def maxSubArray(nums):
    """
    Find the maximum sum of any contiguous subarray.
    
    Args:
        nums: Array of integers
        
    Returns:
        Maximum sum of contiguous subarray
    """
    # TODO: Implement your solution here
    pass


# Test cases
def test_maximum_subarray():
    """Test cases for Maximum Subarray"""
    test_cases = [
        # Basic test cases
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
        
        # Edge cases
        ([-1], -1),
        ([-2, -1], -1),
        ([1, 2, 3, 4, 5], 15),
        ([-5, -4, -3, -2, -1], -1),
        
        # LeetCode test cases
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
        
        # Additional test cases
        ([1, 2, 3, 4, 5], 15),
        ([-1, -2, -3, -4, -5], -1),
        ([1, -1, 1, -1, 1], 1),
        ([1, -2, 3, -4, 5], 5),
        ([0, 0, 0, 0], 0),
        ([1, 0, 0, 0], 1),
        ([0, 0, 0, 1], 1),
        
        # Mixed positive and negative
        ([1, -3, 2, 1, -1], 3),
        ([-1, 3, -2, 1, -1], 2),
        ([1, 2, -1, 3, 4], 9),
        
        # Large numbers
        ([1000000000, -1000000000, 1000000000], 1000000000),
        ([-1000000000, 1000000000, -1000000000], 1000000000),
    ]
    
    print("Testing Maximum Subarray solution...")
    for i, (nums, expected) in enumerate(test_cases):
        result = maxSubArray(nums)
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
    
    # Generate large array with mixed positive and negative numbers
    large_nums = [random.randint(-1000, 1000) for _ in range(10000)]
    
    start_time = time.time()
    result = maxSubArray(large_nums)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large array (10,000 elements): {end_time - start_time:.4f} seconds")
    print(f"Result: {result}")


if __name__ == "__main__":
    test_maximum_subarray()
    test_performance()
