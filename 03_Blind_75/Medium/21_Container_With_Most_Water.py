"""
LeetCode 11. Container With Most Water
Difficulty: Medium
Category: Two Pointers

You are given an integer array height of length n. There are n vertical lines drawn such that 
the two endpoints of the ith line are (i, 0) and (i, height[i]).
Find two lines that together with the x-axis form a container, such that the container contains the most water.
Return the maximum amount of water a container can store.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def maxArea(height):
    """
    Find the maximum area of water that can be contained.
    
    Args:
        height: Array of heights
        
    Returns:
        Maximum area of water
    """
    # TODO: Implement your solution here
    pass


# Test cases
def test_container_with_most_water():
    """Test cases for Container With Most Water"""
    test_cases = [
        # Basic test cases
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        
        # Edge cases
        ([1], 0),
        ([1, 2], 1),
        ([2, 1], 1),
        ([1, 2, 1], 2),
        ([1, 1, 1], 2),
        
        # LeetCode test cases
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        
        # Additional test cases
        ([1, 2, 3, 4, 5], 6),
        ([5, 4, 3, 2, 1], 6),
        ([1, 3, 2, 5, 25, 24, 5], 24),
        ([1, 2, 4, 3], 4),
        ([2, 3, 4, 5, 18, 17, 6], 17),
        
        # Same heights
        ([1, 1, 1, 1], 3),
        ([2, 2, 2, 2], 6),
        ([3, 3, 3, 3], 9),
        
        # Increasing heights
        ([1, 2, 3, 4, 5], 6),
        ([1, 2, 3, 4, 5, 6], 9),
        
        # Decreasing heights
        ([5, 4, 3, 2, 1], 6),
        ([6, 5, 4, 3, 2, 1], 9),
        
        # Large numbers
        ([1000000000, 1000000000], 1000000000),
        ([1, 1000000000, 1000000000, 1], 1000000000),
        
        # Two elements
        ([1, 2], 1),
        ([2, 1], 1),
        ([3, 4], 3),
        ([4, 3], 3),
    ]
    
    print("Testing Container With Most Water solution...")
    for i, (height, expected) in enumerate(test_cases):
        result = maxArea(height)
        if result == expected:
            print(f"✓ Test {i+1} passed: height={height}, result={result}")
        else:
            print(f"✗ Test {i+1} failed: height={height}")
            print(f"  Expected: {expected}, Got: {result}")
    
    print("\nAll tests completed!")


# Performance test
def test_performance():
    """Test solution performance with large input"""
    import time
    import random
    
    # Generate large array
    large_height = [random.randint(1, 1000) for _ in range(10000)]
    
    start_time = time.time()
    result = maxArea(large_height)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large array (10,000 elements): {end_time - start_time:.4f} seconds")
    print(f"Result: {result}")


if __name__ == "__main__":
    test_container_with_most_water()
    test_performance()
