"""
LeetCode 125. Valid Palindrome
Difficulty: Easy
Category: Two Pointers

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters 
and removing all non-alphanumeric characters, it reads the same forward and backward.
Given a string s, return true if it is a palindrome, or false otherwise.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def isPalindrome(s):
    """
    Check if a string is a palindrome after cleaning.
    
    Args:
        s: Input string
        
    Returns:
        Boolean indicating if string is palindrome
    """
    # TODO: Implement your solution here
    pass


# Test cases
def test_valid_palindrome():
    """Test cases for Valid Palindrome"""
    test_cases = [
        # Basic test cases
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("", True),
        
        # Edge cases
        ("a", True),
        ("ab", False),
        ("aba", True),
        ("abba", True),
        ("abcba", True),
        ("abccba", True),
        
        # LeetCode test cases
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        
        # Additional test cases
        ("Madam", True),
        ("No 'x' in Nixon", True),
        ("Was it a car or a cat I saw?", True),
        ("A Santa at NASA", True),
        ("hello", False),
        ("world", False),
        ("12321", True),
        ("12345", False),
        
        # Special characters and numbers
        ("A man, a plan, a canal: Panama!", True),
        ("race a car!", False),
        ("a1b2c3c2b1a", True),
        ("a1b2c3d2b1a", False),
        
        # Mixed case
        ("Aa", True),
        ("Ab", False),
        ("aA", True),
        ("aB", False),
        
        # Only non-alphanumeric
        ("!!!", True),
        ("!@#$%", True),
        ("!@#$%^", False),
    ]
    
    print("Testing Valid Palindrome solution...")
    for i, (s, expected) in enumerate(test_cases):
        result = isPalindrome(s)
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
    import random
    import string
    
    # Generate large palindrome string
    chars = string.ascii_letters + string.digits
    half_length = 5000
    first_half = ''.join(random.choices(chars, k=half_length))
    second_half = first_half[::-1]
    large_palindrome = first_half + second_half
    
    start_time = time.time()
    result = isPalindrome(large_palindrome)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large palindrome (10,000 chars): {end_time - start_time:.4f} seconds")
    print(f"Result: {result}")


if __name__ == "__main__":
    test_valid_palindrome()
    test_performance()
