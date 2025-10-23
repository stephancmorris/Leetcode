"""
LeetCode 22. Generate Parentheses
Difficulty: Medium
Category: Stack

Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Time Complexity: O(4^n / sqrt(n))
Space Complexity: O(4^n / sqrt(n))
"""

def generateParenthesis(n):
    """
    Generate all combinations of well-formed parentheses.
    
    Args:
        n: Number of pairs of parentheses
        
    Returns:
        List of all valid parentheses combinations
    """
    # TODO: Implement your solution here
    pass


# Test cases
def test_generate_parentheses():
    """Test cases for Generate Parentheses"""
    test_cases = [
        # Basic test cases
        (1, ["()"]),
        (2, ["(())", "()()"]),
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        
        # Edge cases
        (0, []),
        (1, ["()"]),
        (2, ["(())", "()()"]),
        
        # LeetCode test cases
        (1, ["()"]),
        (2, ["(())", "()()"]),
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        
        # Additional test cases
        (4, ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"]),
        (5, ["((((()))))", "(((()())))", "(((())()))", "(((()))())", "(((())))()", "((()(())))", "((()()()))", "((()())())", "((()()))()", "((())(()))", "((())()())", "((())())()", "((()))(())", "((()))()()", "(()((())))", "(()(()()))", "(()(())())", "(()(()))()", "(()()(()))", "(()()()())", "(()()())()", "(()())(())", "(()())()()", "(())((()))", "(())(()())", "(())(())()", "(())()(())", "(())()()()", "()(((())))", "()((()()))", "()((())())", "()((()))()", "()(()(()))", "()(()()())", "()(()())()", "()(())(())", "()(())()()", "()()((()))", "()()(()())", "()()(())()", "()()()(())", "()()()()()"]),
        
        # Small values
        (0, []),
        (1, ["()"]),
        (2, ["(())", "()()"]),
        (3, ["((()))", "(()())", "(())()", "()(())", "()()()"]),
        
        # Medium values
        (4, ["(((())))", "((()()))", "((())())", "((()))()", "(()(()))", "(()()())", "(()())()", "(())(())", "(())()()", "()((()))", "()(()())", "()(())()", "()()(())", "()()()()"]),
        (5, ["((((()))))", "(((()())))", "(((())()))", "(((()))())", "(((())))()", "((()(())))", "((()()()))", "((()())())", "((()()))()", "((())(()))", "((())()())", "((())())()", "((()))(())", "((()))()()", "(()((())))", "(()(()()))", "(()(())())", "(()(()))()", "(()()(()))", "(()()()())", "(()()())()", "(()())(())", "(()())()()", "(())((()))", "(())(()())", "(())(())()", "(())()(())", "(())()()()", "()(((())))", "()((()()))", "()((())())", "()((()))()", "()(()(()))", "()(()()())", "()(()())()", "()(())(())", "()(())()()", "()()((()))", "()()(()())", "()()(())()", "()()()(())", "()()()()()"]),
        
        # Large values (just check count)
        (6, None),  # Should have 132 combinations
        (7, None),  # Should have 429 combinations
        (8, None),  # Should have 1430 combinations
        (9, None),  # Should have 4862 combinations
        (10, None), # Should have 16796 combinations
    ]
    
    print("Testing Generate Parentheses solution...")
    for i, (n, expected) in enumerate(test_cases):
        result = generateParenthesis(n)
        
        if expected is None:
            # For large values, just check the count
            expected_count = catalan_number(n)
            if len(result) == expected_count:
                print(f"✓ Test {i+1} passed: n={n}, count={len(result)} (expected {expected_count})")
            else:
                print(f"✗ Test {i+1} failed: n={n}")
                print(f"  Expected count: {expected_count}, Got: {len(result)}")
        else:
            # For small values, check exact matches
            result_sorted = sorted(result)
            expected_sorted = sorted(expected)
            
            if result_sorted == expected_sorted:
                print(f"✓ Test {i+1} passed: n={n}, result={result}")
            else:
                print(f"✗ Test {i+1} failed: n={n}")
                print(f"  Expected: {expected}")
                print(f"  Got: {result}")
    
    print("\nAll tests completed!")


def catalan_number(n):
    """Calculate the nth Catalan number"""
    if n <= 1:
        return 1
    
    result = 1
    for i in range(n):
        result = result * (2 * n - i) // (i + 1)
    
    return result


# Performance test
def test_performance():
    """Test solution performance with large input"""
    import time
    
    # Test with different values of n
    for n in [8, 10, 12]:
        start_time = time.time()
        result = generateParenthesis(n)
        end_time = time.time()
        
        print(f"\nPerformance Test for n={n}:")
        print(f"Time: {end_time - start_time:.4f} seconds")
        print(f"Number of combinations: {len(result)}")
        print(f"First few combinations: {result[:5]}")


if __name__ == "__main__":
    test_generate_parentheses()
    test_performance()
