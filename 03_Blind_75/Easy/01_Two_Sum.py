"""
LeetCode 1. Two Sum
Difficulty: Easy
Category: Arrays & Hashing

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def twoSum(nums, target):
    """
    Find two numbers that add up to target.
    
    Args:
        nums: List of integers
        target: Target sum
        
    Returns:
        List of two indices that sum to target
    """
    # TODO: Implement your solution here
    seen = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i
    return []


# Test cases
def test_two_sum():
    """Test cases for Two Sum problem"""
    test_cases = [
        # Basic test cases
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        
        # Edge cases
        ([1, 2], 3, [0, 1]),
        ([1, 2, 3], 4, [0, 2]),
        
        # Negative numbers
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        ([-1, 0], -1, [0, 1]),
        
        # Large numbers
        ([1000000000, 1000000000], 2000000000, [0, 1]),
        
        # Mixed positive and negative
        ([1, -1, 2, -2], 0, [0, 1]),
    ]
    
    print("Testing Two Sum solution...")
    for i, (nums, target, expected) in enumerate(test_cases):
        result = twoSum(nums, target)
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
    
    # Generate large test case
    large_nums = [random.randint(1, 1000) for _ in range(10000)]
    target = 1999
    
    start_time = time.time()
    result = twoSum(large_nums, target)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large input (10,000 elements): {end_time - start_time:.4f} seconds")
    print(f"Result: {result}")


if __name__ == "__main__":
    test_two_sum()
    test_performance()

