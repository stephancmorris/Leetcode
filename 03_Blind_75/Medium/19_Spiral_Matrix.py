"""
LeetCode 54. Spiral Matrix
Difficulty: Medium
Category: Arrays & Hashing

Given an m x n matrix, return all elements of the matrix in spiral order.

Time Complexity: O(m * n)
Space Complexity: O(1) excluding output
"""

def spiralOrder(matrix):
    """
    Return all elements of matrix in spiral order.
    
    Args:
        matrix: 2D array of integers
        
    Returns:
        List of elements in spiral order
    """
    # TODO: Implement your solution here
    pass


# Test cases
def test_spiral_matrix():
    """Test cases for Spiral Matrix"""
    test_cases = [
        # Basic test cases
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
        
        # Edge cases
        ([[1]], [1]),
        ([[1, 2]], [1, 2]),
        ([[1], [2]], [1, 2]),
        ([[1, 2], [3, 4]], [1, 2, 4, 3]),
        ([], []),
        ([[], []], []),
        
        # LeetCode test cases
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]], [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]),
        
        # Additional test cases
        ([[1, 2, 3, 4, 5]], [1, 2, 3, 4, 5]),
        ([[1], [2], [3], [4], [5]], [1, 2, 3, 4, 5]),
        ([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]], [1, 2, 3, 4, 5, 10, 9, 8, 7, 6]),
        
        # Single row
        ([[1, 2, 3, 4, 5]], [1, 2, 3, 4, 5]),
        ([[1, 2, 3, 4, 5, 6]], [1, 2, 3, 4, 5, 6]),
        
        # Single column
        ([[1], [2], [3], [4], [5]], [1, 2, 3, 4, 5]),
        ([[1], [2], [3], [4], [5], [6]], [1, 2, 3, 4, 5, 6]),
        
        # 2x2 matrix
        ([[1, 2], [3, 4]], [1, 2, 4, 3]),
        ([[1, 2], [4, 3]], [1, 2, 3, 4]),
        
        # 3x3 matrix
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [1, 2, 3, 6, 9, 8, 7, 4, 5]),
        ([[1, 2, 3], [8, 9, 4], [7, 6, 5]], [1, 2, 3, 4, 5, 6, 7, 8, 9]),
        
        # 4x4 matrix
        ([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 
         [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]),
        
        # Large matrix
        ([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]], 
         [1, 2, 3, 4, 5, 6, 12, 18, 17, 16, 15, 14, 13, 7, 8, 9, 10, 11]),
        
        # Negative numbers
        ([[-1, -2, -3], [-4, -5, -6], [-7, -8, -9]], [-1, -2, -3, -6, -9, -8, -7, -4, -5]),
        
        # Mixed positive and negative
        ([[1, -2, 3], [-4, 5, -6], [7, -8, 9]], [1, -2, 3, -6, 9, -8, 7, -4, 5]),
        
        # Zero
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [0, 0, 0, 0, 0, 0, 0, 0, 0]),
        
        # Large numbers
        ([[1000000000, 2000000000], [3000000000, 4000000000]], [1000000000, 2000000000, 4000000000, 3000000000]),
    ]
    
    print("Testing Spiral Matrix solution...")
    for i, (matrix, expected) in enumerate(test_cases):
        result = spiralOrder(matrix)
        if result == expected:
            print(f"✓ Test {i+1} passed: matrix={matrix}, result={result}")
        else:
            print(f"✗ Test {i+1} failed: matrix={matrix}")
            print(f"  Expected: {expected}, Got: {result}")
    
    print("\nAll tests completed!")


# Performance test
def test_performance():
    """Test solution performance with large matrix"""
    import time
    
    # Generate large matrix
    large_matrix = [[i + j for j in range(100)] for i in range(100)]
    
    start_time = time.time()
    result = spiralOrder(large_matrix)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large matrix (100x100): {end_time - start_time:.4f} seconds")
    print(f"Result length: {len(result)}")


if __name__ == "__main__":
    test_spiral_matrix()
    test_performance()
