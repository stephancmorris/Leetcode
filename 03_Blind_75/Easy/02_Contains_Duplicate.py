"""
LeetCode 217. Contains Duplicate
Difficulty: Easy
Category: Arrays & Hashing

Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def containsDuplicate(nums):
    """
    Check if array contains any duplicate values.
    
    Args:
        nums: Array of integers
        
    Returns:
        Boolean indicating if array contains duplicates
    """
    # TODO: Implement your solution here
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# Test cases
def test_contains_duplicate():
    """Test cases for Contains Duplicate"""
    test_cases = [
        # Basic test cases
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        
        # Edge cases
        ([1], False),
        ([], False),
        ([1, 2], False),
        ([1, 1], True),
        
        # LeetCode test cases
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        
        # Additional edge cases
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], False),
        ([1, 1, 2, 2, 3, 3], True),
        ([-1, -2, -3, -1], True),
        ([0, 0], True),
    ]
    
    print("Testing Contains Duplicate solution...")
    for i, (nums, expected) in enumerate(test_cases):
        result = containsDuplicate(nums)
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
    
    # Generate large test case with duplicates
    large_nums = [random.randint(1, 1000) for _ in range(10000)]
    # Add some duplicates
    large_nums.extend([1, 2, 3, 1])  # This will have duplicates
    
    start_time = time.time()
    result = containsDuplicate(large_nums)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large input (10,004 elements): {end_time - start_time:.4f} seconds")
    print(f"Result: {result}")


if __name__ == "__main__":
    test_contains_duplicate()
    test_performance()
