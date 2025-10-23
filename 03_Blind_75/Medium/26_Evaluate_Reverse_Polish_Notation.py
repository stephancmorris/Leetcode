"""
LeetCode 150. Evaluate Reverse Polish Notation
Difficulty: Medium
Category: Stack

You are given an array of strings tokens that represents an arithmetic expression in a 
Reverse Polish Notation.
Evaluate the expression. Return an integer that represents the value of the expression.

Time Complexity: O(n)
Space Complexity: O(n)
"""

def evalRPN(tokens):
    """
    Evaluate Reverse Polish Notation expression.
    
    Args:
        tokens: Array of strings representing RPN expression
        
    Returns:
        Result of the expression
    """
    # TODO: Implement your solution here
    pass


# Test cases
def test_evaluate_reverse_polish_notation():
    """Test cases for Evaluate Reverse Polish Notation"""
    test_cases = [
        # Basic test cases
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
        
        # Edge cases
        (["1"], 1),
        (["0"], 0),
        (["-1"], -1),
        (["2", "1", "+"], 3),
        (["2", "1", "-"], 1),
        (["2", "1", "*"], 2),
        (["2", "1", "/"], 2),
        
        # LeetCode test cases
        (["2", "1", "+", "3", "*"], 9),
        (["4", "13", "5", "/", "+"], 6),
        (["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"], 22),
        
        # Additional test cases
        (["1", "2", "+"], 3),
        (["1", "2", "-"], -1),
        (["1", "2", "*"], 2),
        (["1", "2", "/"], 0),
        (["2", "1", "/"], 2),
        (["3", "2", "/"], 1),
        (["4", "2", "/"], 2),
        (["5", "2", "/"], 2),
        (["6", "2", "/"], 3),
        
        # Negative numbers
        (["-1", "2", "+"], 1),
        (["-1", "2", "-"], -3),
        (["-1", "2", "*"], -2),
        (["-1", "2", "/"], 0),
        (["2", "-1", "+"], 1),
        (["2", "-1", "-"], 3),
        (["2", "-1", "*"], -2),
        (["2", "-1", "/"], -2),
        
        # Multiple operations
        (["1", "2", "+", "3", "+"], 6),
        (["1", "2", "+", "3", "-"], 0),
        (["1", "2", "+", "3", "*"], 9),
        (["1", "2", "+", "3", "/"], 1),
        (["1", "2", "-", "3", "+"], 2),
        (["1", "2", "-", "3", "-"], -4),
        (["1", "2", "-", "3", "*"], -3),
        (["1", "2", "-", "3", "/"], 0),
        
        # Complex expressions
        (["1", "2", "3", "+", "*"], 5),
        (["1", "2", "3", "+", "/"], 0),
        (["1", "2", "3", "-", "*"], -1),
        (["1", "2", "3", "-", "/"], -1),
        (["1", "2", "3", "*", "+"], 7),
        (["1", "2", "3", "*", "-"], -5),
        (["1", "2", "3", "/", "+"], 1),
        (["1", "2", "3", "/", "-"], 1),
        
        # Large numbers
        (["1000000000", "1000000000", "+"], 2000000000),
        (["1000000000", "1000000000", "-"], 0),
        (["1000000000", "1000000000", "*"], 1000000000000000000),
        (["1000000000", "1000000000", "/"], 1),
        
        # Very large numbers
        (["2147483647", "1", "+"], 2147483648),
        (["2147483647", "1", "-"], 2147483646),
        (["2147483647", "2", "*"], 4294967294),
        (["2147483647", "2", "/"], 1073741823),
        
        # Zero operations
        (["0", "1", "+"], 1),
        (["0", "1", "-"], -1),
        (["0", "1", "*"], 0),
        (["0", "1", "/"], 0),
        (["1", "0", "+"], 1),
        (["1", "0", "-"], 1),
        (["1", "0", "*"], 0),
        (["1", "0", "/"], 0),  # Division by zero should be handled
        
        # Single digit operations
        (["0", "0", "+"], 0),
        (["0", "0", "-"], 0),
        (["0", "0", "*"], 0),
        (["0", "0", "/"], 0),  # Division by zero should be handled
        
        # Mixed positive and negative
        (["1", "-1", "+"], 0),
        (["1", "-1", "-"], 2),
        (["1", "-1", "*"], -1),
        (["1", "-1", "/"], -1),
        (["-1", "1", "+"], 0),
        (["-1", "1", "-"], -2),
        (["-1", "1", "*"], -1),
        (["-1", "1", "/"], -1),
        
        # Complex nested expressions
        (["1", "2", "+", "3", "4", "+", "*"], 21),
        (["1", "2", "+", "3", "4", "+", "/"], 0),
        (["1", "2", "-", "3", "4", "-", "*"], 1),
        (["1", "2", "-", "3", "4", "-", "/"], 1),
        
        # Edge cases with division
        (["1", "2", "/"], 0),
        (["2", "1", "/"], 2),
        (["3", "2", "/"], 1),
        (["4", "2", "/"], 2),
        (["5", "2", "/"], 2),
        (["6", "2", "/"], 3),
        (["7", "2", "/"], 3),
        (["8", "2", "/"], 4),
        (["9", "2", "/"], 4),
        (["10", "2", "/"], 5),
        
        # Very long expressions
        (["1"] + ["2"] * 100 + ["+"] * 100, 201),
        (["1"] + ["2"] * 100 + ["-"] * 100, -199),
        (["1"] + ["2"] * 100 + ["*"] * 100, 1),
        (["1"] + ["2"] * 100 + ["/"] * 100, 0),
    ]
    
    print("Testing Evaluate Reverse Polish Notation solution...")
    for i, (tokens, expected) in enumerate(test_cases):
        try:
            result = evalRPN(tokens)
            if result == expected:
                print(f"✓ Test {i+1} passed: tokens={tokens}, result={result}")
            else:
                print(f"✗ Test {i+1} failed: tokens={tokens}")
                print(f"  Expected: {expected}, Got: {result}")
        except Exception as e:
            print(f"✗ Test {i+1} failed: tokens={tokens}")
            print(f"  Expected: {expected}, Got: Exception - {e}")
    
    print("\nAll tests completed!")


# Performance test
def test_performance():
    """Test solution performance with large input"""
    import time
    import random
    
    # Generate large RPN expression
    large_tokens = []
    for i in range(1000):
        large_tokens.append(str(random.randint(1, 100)))
        if i > 0 and i % 2 == 1:
            large_tokens.append(random.choice(["+", "-", "*", "/"]))
    
    start_time = time.time()
    result = evalRPN(large_tokens)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large RPN expression (1,000 tokens): {end_time - start_time:.4f} seconds")
    print(f"Result: {result}")


if __name__ == "__main__":
    test_evaluate_reverse_polish_notation()
    test_performance()
