"""
LeetCode 75. Sort Colors
Difficulty: Medium
Category: Two Pointers

Given an array nums with n objects colored red, white, or blue, sort them in-place so that 
objects of the same color are adjacent, with the colors in the order red, white, and blue.
We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.
You must solve this problem without using the library's sort function.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def sortColors(nums):
    """
    Sort array of colors (0=red, 1=white, 2=blue) in-place.
    
    Args:
        nums: Array of integers (0, 1, 2) representing colors
    """
    # TODO: Implement your solution here
    pass


# Test cases
def test_sort_colors():
    """Test cases for Sort Colors"""
    test_cases = [
        # Basic test cases
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
        ([0], [0]),
        ([1], [1]),
        ([2], [2]),
        
        # Edge cases
        ([], []),
        ([0, 0], [0, 0]),
        ([1, 1], [1, 1]),
        ([2, 2], [2, 2]),
        ([0, 1], [0, 1]),
        ([0, 2], [0, 2]),
        ([1, 0], [0, 1]),
        ([1, 2], [1, 2]),
        ([2, 0], [0, 2]),
        ([2, 1], [1, 2]),
        
        # LeetCode test cases
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
        
        # Additional test cases
        ([0, 0, 0], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1]),
        ([2, 2, 2], [2, 2, 2]),
        ([0, 1, 2], [0, 1, 2]),
        ([2, 1, 0], [0, 1, 2]),
        ([1, 0, 2], [0, 1, 2]),
        ([1, 2, 0], [0, 1, 2]),
        ([0, 2, 1], [0, 1, 2]),
        
        # All zeros
        ([0, 0, 0, 0], [0, 0, 0, 0]),
        ([0, 0, 0, 0, 0], [0, 0, 0, 0, 0]),
        
        # All ones
        ([1, 1, 1, 1], [1, 1, 1, 1]),
        ([1, 1, 1, 1, 1], [1, 1, 1, 1, 1]),
        
        # All twos
        ([2, 2, 2, 2], [2, 2, 2, 2]),
        ([2, 2, 2, 2, 2], [2, 2, 2, 2, 2]),
        
        # Mixed patterns
        ([0, 1, 2, 0, 1, 2], [0, 0, 1, 1, 2, 2]),
        ([2, 1, 0, 2, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([1, 0, 2, 1, 0, 2], [0, 0, 1, 1, 2, 2]),
        ([0, 2, 1, 0, 2, 1], [0, 0, 1, 1, 2, 2]),
        
        # Large arrays
        ([0, 1, 2] * 100, [0] * 100 + [1] * 100 + [2] * 100),
        ([2, 1, 0] * 100, [0] * 100 + [1] * 100 + [2] * 100),
        ([1, 0, 2] * 100, [0] * 100 + [1] * 100 + [2] * 100),
        
        # Single color arrays
        ([0] * 100, [0] * 100),
        ([1] * 100, [1] * 100),
        ([2] * 100, [2] * 100),
        
        # Two colors
        ([0, 1] * 50, [0] * 50 + [1] * 50),
        ([1, 0] * 50, [0] * 50 + [1] * 50),
        ([0, 2] * 50, [0] * 50 + [2] * 50),
        ([2, 0] * 50, [0] * 50 + [2] * 50),
        ([1, 2] * 50, [1] * 50 + [2] * 50),
        ([2, 1] * 50, [1] * 50 + [2] * 50),
        
        # Complex patterns
        ([0, 1, 2, 0, 1, 2, 0, 1, 2], [0, 0, 0, 1, 1, 1, 2, 2, 2]),
        ([2, 1, 0, 2, 1, 0, 2, 1, 0], [0, 0, 0, 1, 1, 1, 2, 2, 2]),
        ([1, 0, 2, 1, 0, 2, 1, 0, 2], [0, 0, 0, 1, 1, 1, 2, 2, 2]),
        
        # Edge cases with duplicates
        ([0, 0, 1, 1, 2, 2], [0, 0, 1, 1, 2, 2]),
        ([2, 2, 1, 1, 0, 0], [0, 0, 1, 1, 2, 2]),
        ([1, 1, 0, 0, 2, 2], [0, 0, 1, 1, 2, 2]),
        ([0, 0, 2, 2, 1, 1], [0, 0, 1, 1, 2, 2]),
        ([2, 2, 0, 0, 1, 1], [0, 0, 1, 1, 2, 2]),
        ([1, 1, 2, 2, 0, 0], [0, 0, 1, 1, 2, 2]),
    ]
    
    print("Testing Sort Colors solution...")
    for i, (nums, expected) in enumerate(test_cases):
        # Create a copy of the array for testing
        test_nums = nums[:]
        sortColors(test_nums)
        
        if test_nums == expected:
            print(f"✓ Test {i+1} passed: nums={nums}, result={test_nums}")
        else:
            print(f"✗ Test {i+1} failed: nums={nums}")
            print(f"  Expected: {expected}, Got: {test_nums}")
    
    print("\nAll tests completed!")


# Performance test
def test_performance():
    """Test solution performance with large input"""
    import time
    import random
    
    # Generate large array with random 0s, 1s, and 2s
    large_nums = [random.randint(0, 2) for _ in range(10000)]
    
    start_time = time.time()
    sortColors(large_nums)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large array (10,000 elements): {end_time - start_time:.4f} seconds")
    print(f"Sorted array: {large_nums[:20]}... (showing first 20 elements)")


if __name__ == "__main__":
    test_sort_colors()
    test_performance()
