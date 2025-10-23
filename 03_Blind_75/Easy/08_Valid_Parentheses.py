"""
LeetCode 20. Valid Parentheses
Difficulty: Easy
Category: Stack

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.
An input string is valid if:
1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def isValid(s):
    """
    Check if parentheses string is valid.
    
    Args:
        s: String containing only parentheses characters
        
    Returns:
        Boolean indicating if parentheses are valid
    """
    # TODO: Implement your solution here
    pass


# Test cases
def test_valid_parentheses():
    """Test cases for Valid Parentheses"""
    test_cases = [
        # Basic test cases
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        
        # Edge cases
        ("", True),
        ("(", False),
        (")", False),
        ("[", False),
        ("]", False),
        ("{", False),
        ("}", False),
        
        # LeetCode test cases
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        
        # Additional test cases
        ("([{}])", True),
        ("([)]", False),
        ("{[]}", True),
        ("((()))", True),
        ("((())", False),
        ("(()))", False),
        ("([{}])", True),
        ("([{])", False),
        
        # Nested parentheses
        ("((()))", True),
        ("((())", False),
        ("(()))", False),
        ("((())))", False),
        
        # Mixed types
        ("()[]{}", True),
        ("([{}])", True),
        ("([)]", False),
        ("{[]}", True),
        ("{[}]", False),
        
        # Complex cases
        ("(([]))", True),
        ("(([))", False),
        ("(([]))", True),
        ("(([))", False),
        
        # Single characters
        ("(", False),
        (")", False),
        ("[", False),
        ("]", False),
        ("{", False),
        ("}", False),
        
        # Multiple same type
        ("((()))", True),
        ("((())", False),
        ("(()))", False),
        ("((())))", False),
    ]
    
    print("Testing Valid Parentheses solution...")
    for i, (s, expected) in enumerate(test_cases):
        result = isValid(s)
        if result == expected:
            print(f"✓ Test {i+1} passed: s='{s}', result={result}")
        else:
            print(f"✗ Test {i+1} failed: s='{s}'")
            print(f"  Expected: {expected}, Got: {result}")
    
    print("\nAll tests completed!")


# Performance test
def test_performance():
    """Test solution performance with large input"""
    import time
    
    # Generate large valid parentheses string
    large_valid = "(" * 5000 + ")" * 5000  # Valid but not properly nested
    large_invalid = "(" * 5000 + ")" * 4999  # Invalid
    
    start_time = time.time()
    result1 = isValid(large_valid)
    end_time = time.time()
    
    start_time2 = time.time()
    result2 = isValid(large_invalid)
    end_time2 = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large valid string (10,000 chars): {end_time - start_time:.4f} seconds, result={result1}")
    print(f"Large invalid string (9,999 chars): {end_time2 - start_time2:.4f} seconds, result={result2}")


if __name__ == "__main__":
    test_valid_parentheses()
    test_performance()
