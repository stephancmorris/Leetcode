"""
LeetCode 167. Two Sum II - Input Array Is Sorted
Difficulty: Easy
Category: Two Pointers

Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, 
find two numbers such that they add up to a specific target number. Let these two numbers be 
numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
Return the indices of the two numbers, index1 and index2, added by one as an integer array 
[index1, index2] of length 2.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def twoSum(numbers, target):
    """
    Find two numbers that add up to target in sorted array.
    
    Args:
        numbers: Sorted array of integers
        target: Target sum
        
    Returns:
        List of two indices (1-indexed) that sum to target
    """
    # TODO: Implement your solution here
    pass


# Test cases
def test_two_sum_ii():
    """Test cases for Two Sum II"""
    test_cases = [
        # Basic test cases
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        
        # Edge cases
        ([1, 2], 3, [1, 2]),
        ([1, 2, 3], 4, [1, 3]),
        ([1, 2, 3, 4], 5, [1, 4]),
        
        # LeetCode test cases
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        
        # Additional test cases
        ([1, 2, 3, 4, 5], 8, [3, 5]),
        ([1, 2, 3, 4, 5], 9, [4, 5]),
        ([1, 2, 3, 4, 5], 3, [1, 2]),
        
        # Negative numbers
        ([-5, -4, -3, -2, -1], -8, [1, 5]),
        ([-3, -2, -1, 0, 1], -2, [1, 4]),
        
        # Large numbers
        ([1000000000, 1000000000], 2000000000, [1, 2]),
        
        # Duplicates
        ([1, 1, 2, 3], 2, [1, 2]),
        ([1, 1, 2, 3], 3, [1, 3]),
        ([1, 1, 2, 3], 4, [2, 4]),
        
        # Single valid pair
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 11, [1, 10]),
    ]
    
    print("Testing Two Sum II solution...")
    for i, (numbers, target, expected) in enumerate(test_cases):
        result = twoSum(numbers, target)
        if result == expected:
            print(f"✓ Test {i+1} passed: numbers={numbers}, target={target}, result={result}")
        else:
            print(f"✗ Test {i+1} failed: numbers={numbers}, target={target}")
            print(f"  Expected: {expected}, Got: {result}")
    
    print("\nAll tests completed!")


# Performance test
def test_performance():
    """Test solution performance with large input"""
    import time
    
    # Generate large sorted array
    large_numbers = list(range(1, 10001))  # [1, 2, 3, ..., 10000]
    target = 19999  # Sum of first and last elements
    
    start_time = time.time()
    result = twoSum(large_numbers, target)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large sorted array (10,000 elements): {end_time - start_time:.4f} seconds")
    print(f"Result: {result}")


if __name__ == "__main__":
    test_two_sum_ii()
    test_performance()
