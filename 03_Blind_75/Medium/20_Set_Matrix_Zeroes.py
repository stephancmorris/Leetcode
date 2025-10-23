"""
LeetCode 73. Set Matrix Zeroes
Difficulty: Medium
Category: Arrays & Hashing

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place.

Time Complexity: O(m * n)
Space Complexity: O(1)
"""

def setZeroes(matrix):
    """
    Set entire row and column to 0 if element is 0.
    
    Args:
        matrix: 2D array of integers (modified in place)
    """
    # TODO: Implement your solution here
    pass


# Test cases
def test_set_matrix_zeroes():
    """Test cases for Set Matrix Zeroes"""
    test_cases = [
        # Basic test cases
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
        ([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]),
        
        # Edge cases
        ([[1]], [[1]]),
        ([[0]], [[0]]),
        ([[1, 0]], [[0, 0]]),
        ([[1], [0]], [[0], [0]]),
        ([[0, 0], [0, 0]], [[0, 0], [0, 0]]),
        ([[1, 1], [1, 1]], [[1, 1], [1, 1]]),
        
        # LeetCode test cases
        ([[1, 1, 1], [1, 0, 1], [1, 1, 1]], [[1, 0, 1], [0, 0, 0], [1, 0, 1]]),
        ([[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]], [[0, 0, 0, 0], [0, 4, 5, 0], [0, 3, 1, 0]]),
        
        # Additional test cases
        ([[1, 2, 3], [4, 0, 6], [7, 8, 9]], [[1, 0, 3], [0, 0, 0], [7, 0, 9]]),
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        
        # Single row
        ([[1, 0, 3]], [[0, 0, 0]]),
        ([[1, 2, 3]], [[1, 2, 3]]),
        ([[0, 0, 0]], [[0, 0, 0]]),
        
        # Single column
        ([[1], [0], [3]], [[0], [0], [0]]),
        ([[1], [2], [3]], [[1], [2], [3]]),
        ([[0], [0], [0]], [[0], [0], [0]]),
        
        # 2x2 matrix
        ([[1, 0], [3, 4]], [[0, 0], [3, 0]]),
        ([[0, 1], [3, 4]], [[0, 0], [0, 4]]),
        ([[1, 2], [0, 4]], [[0, 2], [0, 0]]),
        ([[1, 2], [3, 0]], [[1, 0], [0, 0]]),
        
        # 3x3 matrix
        ([[1, 2, 3], [4, 0, 6], [7, 8, 9]], [[1, 0, 3], [0, 0, 0], [7, 0, 9]]),
        ([[0, 2, 3], [4, 5, 6], [7, 8, 9]], [[0, 0, 0], [0, 5, 6], [0, 8, 9]]),
        ([[1, 2, 0], [4, 5, 6], [7, 8, 9]], [[0, 0, 0], [4, 5, 0], [7, 8, 0]]),
        ([[1, 2, 3], [4, 5, 6], [0, 8, 9]], [[0, 2, 3], [0, 5, 6], [0, 0, 0]]),
        
        # 4x4 matrix
        ([[1, 2, 3, 4], [5, 0, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 
         [[1, 0, 3, 4], [0, 0, 0, 0], [9, 0, 11, 12], [13, 0, 15, 16]]),
        
        # Multiple zeros
        ([[1, 0, 3], [0, 5, 6], [7, 8, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
        ([[0, 1, 0], [3, 4, 5], [0, 7, 8]], [[0, 0, 0], [0, 4, 0], [0, 0, 0]]),
        
        # All zeros
        ([[0, 0, 0], [0, 0, 0], [0, 0, 0]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]),
        
        # No zeros
        ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
        
        # Large matrix
        ([[1, 2, 3, 4, 5], [6, 7, 0, 9, 10], [11, 12, 13, 14, 15]], 
         [[1, 2, 0, 4, 5], [0, 0, 0, 0, 0], [11, 12, 0, 14, 15]]),
        
        # Negative numbers
        ([[-1, -2, -3], [-4, 0, -6], [-7, -8, -9]], [[-1, 0, -3], [0, 0, 0], [-7, 0, -9]]),
        
        # Mixed positive and negative
        ([[1, -2, 3], [-4, 0, 6], [7, -8, 9]], [[1, 0, 3], [0, 0, 0], [7, 0, 9]]),
        
        # Large numbers
        ([[1000000000, 2000000000], [0, 4000000000]], [[0, 0], [0, 0]]),
    ]
    
    print("Testing Set Matrix Zeroes solution...")
    for i, (matrix, expected) in enumerate(test_cases):
        # Create a copy of the matrix for testing
        test_matrix = [row[:] for row in matrix]
        setZeroes(test_matrix)
        
        if test_matrix == expected:
            print(f"✓ Test {i+1} passed: matrix={matrix}, result={test_matrix}")
        else:
            print(f"✗ Test {i+1} failed: matrix={matrix}")
            print(f"  Expected: {expected}, Got: {test_matrix}")
    
    print("\nAll tests completed!")


# Performance test
def test_performance():
    """Test solution performance with large matrix"""
    import time
    
    # Generate large matrix with some zeros
    large_matrix = [[i + j if (i + j) % 10 != 0 else 0 for j in range(100)] for i in range(100)]
    
    start_time = time.time()
    setZeroes(large_matrix)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large matrix (100x100): {end_time - start_time:.4f} seconds")


if __name__ == "__main__":
    test_set_matrix_zeroes()
    test_performance()
