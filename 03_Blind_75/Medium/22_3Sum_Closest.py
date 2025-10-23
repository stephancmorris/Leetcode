"""
LeetCode 16. 3Sum Closest
Difficulty: Medium
Category: Two Pointers

Given an integer array nums of length n and an integer target, find three integers in nums 
such that the sum is closest to target. Return the sum of the three integers.
You may assume that each input would have exactly one solution.

Time Complexity: O(n^2)
Space Complexity: O(1)
"""

def threeSumClosest(nums, target):
    """
    Find three integers whose sum is closest to target.
    
    Args:
        nums: Array of integers
        target: Target sum
        
    Returns:
        Sum of three integers closest to target
    """
    # TODO: Implement your solution here
    pass


# Test cases
def test_three_sum_closest():
    """Test cases for 3Sum Closest"""
    test_cases = [
        # Basic test cases
        ([-1, 2, 1, -4], 1, 2),
        ([0, 0, 0], 1, 0),
        ([1, 1, 1, 0], -100, 2),
        
        # Edge cases
        ([1, 1, 1], 1, 3),
        ([1, 1, 1], 2, 3),
        ([1, 1, 1], 3, 3),
        ([1, 1, 1], 4, 3),
        ([1, 1, 1], 0, 3),
        ([1, 1, 1], -1, 3),
        
        # LeetCode test cases
        ([-1, 2, 1, -4], 1, 2),
        ([0, 0, 0], 1, 0),
        
        # Additional test cases
        ([1, 2, 3, 4, 5], 10, 9),
        ([1, 2, 3, 4, 5], 15, 12),
        ([1, 2, 3, 4, 5], 5, 6),
        ([1, 2, 3, 4, 5], 0, 6),
        ([1, 2, 3, 4, 5], 20, 12),
        
        # Negative numbers
        ([-1, -2, -3, -4, -5], -10, -6),
        ([-1, -2, -3, -4, -5], -15, -6),
        ([-1, -2, -3, -4, -5], -5, -6),
        ([-1, -2, -3, -4, -5], 0, -6),
        ([-1, -2, -3, -4, -5], -20, -6),
        
        # Mixed positive and negative
        ([-1, 2, 1, -4], 0, 0),
        ([-1, 2, 1, -4], -1, -1),
        ([-1, 2, 1, -4], 1, 2),
        ([-1, 2, 1, -4], 2, 2),
        ([-1, 2, 1, -4], 3, 2),
        
        # Duplicates
        ([1, 1, 1, 1], 3, 3),
        ([1, 1, 1, 1], 2, 3),
        ([1, 1, 1, 1], 4, 3),
        ([1, 1, 1, 1], 0, 3),
        ([1, 1, 1, 1], 5, 3),
        
        # Large numbers
        ([1000000000, -1000000000, 1000000000], 0, 1000000000),
        ([1000000000, -1000000000, 1000000000], 1000000000, 1000000000),
        ([1000000000, -1000000000, 1000000000], -1000000000, -1000000000),
        
        # Three elements
        ([1, 2, 3], 6, 6),
        ([1, 2, 3], 5, 6),
        ([1, 2, 3], 7, 6),
        ([1, 2, 3], 0, 6),
        ([1, 2, 3], 10, 6),
        
        # Four elements
        ([1, 2, 3, 4], 6, 6),
        ([1, 2, 3, 4], 7, 6),
        ([1, 2, 3, 4], 8, 9),
        ([1, 2, 3, 4], 5, 6),
        ([1, 2, 3, 4], 9, 9),
        
        # All zeros
        ([0, 0, 0], 0, 0),
        ([0, 0, 0], 1, 0),
        ([0, 0, 0], -1, 0),
        ([0, 0, 0], 100, 0),
        ([0, 0, 0], -100, 0),
        
        # Single element repeated
        ([1, 1, 1], 0, 3),
        ([1, 1, 1], 1, 3),
        ([1, 1, 1], 2, 3),
        ([1, 1, 1], 3, 3),
        ([1, 1, 1], 4, 3),
        
        # Two elements repeated
        ([1, 1, 2, 2], 3, 4),
        ([1, 1, 2, 2], 4, 4),
        ([1, 1, 2, 2], 5, 4),
        ([1, 1, 2, 2], 2, 4),
        ([1, 1, 2, 2], 6, 4),
    ]
    
    print("Testing 3Sum Closest solution...")
    for i, (nums, target, expected) in enumerate(test_cases):
        result = threeSumClosest(nums, target)
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
    
    # Generate large array
    large_nums = [random.randint(-1000, 1000) for _ in range(1000)]
    target = random.randint(-3000, 3000)
    
    start_time = time.time()
    result = threeSumClosest(large_nums, target)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large array (1,000 elements): {end_time - start_time:.4f} seconds")
    print(f"Result: {result}")


if __name__ == "__main__":
    test_three_sum_closest()
    test_performance()
