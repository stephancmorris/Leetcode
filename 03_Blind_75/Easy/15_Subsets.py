"""
LeetCode 78. Subsets
Difficulty: Easy
Category: Backtracking

Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets. Return the solution in any order.

Time Complexity: O(2^n * n)
Space Complexity: O(2^n * n)
"""

def subsets(nums):
    """
    Generate all possible subsets of the given array.
    
    Args:
        nums: Array of unique integers
        
    Returns:
        List of all possible subsets
    """
    # TODO: Implement your solution here
    pass


# Test cases
def test_subsets():
    """Test cases for Subsets"""
    test_cases = [
        # Basic test cases
        ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
        ([0], [[], [0]]),
        
        # Edge cases
        ([], [[]]),
        ([1], [[], [1]]),
        ([1, 2], [[], [1], [2], [1, 2]]),
        
        # LeetCode test cases
        ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
        ([0], [[], [0]]),
        
        # Additional test cases
        ([1, 2, 3, 4], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3], [4], [1, 4], [2, 4], [1, 2, 4], [3, 4], [1, 3, 4], [2, 3, 4], [1, 2, 3, 4]]),
        
        # Negative numbers
        ([-1, 0, 1], [[], [-1], [0], [-1, 0], [1], [-1, 1], [0, 1], [-1, 0, 1]]),
        
        # Large numbers
        ([1000000000, 2000000000], [[], [1000000000], [2000000000], [1000000000, 2000000000]]),
        
        # Single element
        ([42], [[], [42]]),
        
        # Two elements
        ([1, 2], [[], [1], [2], [1, 2]]),
        
        # Three elements
        ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
    ]
    
    print("Testing Subsets solution...")
    for i, (nums, expected) in enumerate(test_cases):
        result = subsets(nums)
        # Sort each subset and the overall result for comparison
        result_sorted = [sorted(subset) for subset in result]
        result_sorted.sort()
        expected_sorted = [sorted(subset) for subset in expected]
        expected_sorted.sort()
        
        if result_sorted == expected_sorted:
            print(f"✓ Test {i+1} passed: nums={nums}")
            print(f"  Number of subsets: {len(result)}")
        else:
            print(f"✗ Test {i+1} failed: nums={nums}")
            print(f"  Expected {len(expected)} subsets, Got {len(result)} subsets")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")
    
    print("\nAll tests completed!")


# Performance test
def test_performance():
    """Test solution performance with large input"""
    import time
    
    # Generate large array
    large_nums = list(range(1, 11))  # [1, 2, 3, ..., 10]
    
    start_time = time.time()
    result = subsets(large_nums)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large array (10 elements): {end_time - start_time:.4f} seconds")
    print(f"Number of subsets: {len(result)}")
    print(f"Expected number of subsets: {2**10}")


if __name__ == "__main__":
    test_subsets()
    test_performance()
