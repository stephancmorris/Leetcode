"""
LeetCode 424. Longest Repeating Character Replacement
Difficulty: Medium
Category: Sliding Window

You are given a string s and an integer k. You can choose any character of the string and 
change it to any other uppercase English letter. You can perform this operation at most k times.
Return the length of the longest substring containing the same letter you can get after 
performing the above operations.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def characterReplacement(s, k):
    """
    Find longest substring with same character after k replacements.
    
    Args:
        s: Input string
        k: Maximum number of replacements allowed
        
    Returns:
        Length of longest substring with same character
    """
    # TODO: Implement your solution here
    pass


# Test cases
def test_longest_repeating_character_replacement():
    """Test cases for Longest Repeating Character Replacement"""
    test_cases = [
        # Basic test cases
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        ("AABABBA", 2, 5),
        ("AABABBA", 3, 6),
        ("AABABBA", 4, 7),
        
        # Edge cases
        ("", 0, 0),
        ("A", 0, 1),
        ("A", 1, 1),
        ("AA", 0, 2),
        ("AA", 1, 2),
        ("AB", 0, 1),
        ("AB", 1, 2),
        ("AB", 2, 2),
        
        # LeetCode test cases
        ("ABAB", 2, 4),
        ("AABABBA", 1, 4),
        
        # Additional test cases
        ("AABABBA", 0, 2),
        ("AABABBA", 1, 4),
        ("AABABBA", 2, 5),
        ("AABABBA", 3, 6),
        ("AABABBA", 4, 7),
        ("AABABBA", 5, 7),
        ("AABABBA", 6, 7),
        ("AABABBA", 7, 7),
        
        # Single character
        ("A", 0, 1),
        ("A", 1, 1),
        ("A", 2, 1),
        ("A", 10, 1),
        
        # All same characters
        ("AAAA", 0, 4),
        ("AAAA", 1, 4),
        ("AAAA", 2, 4),
        ("AAAA", 10, 4),
        
        # All different characters
        ("ABCD", 0, 1),
        ("ABCD", 1, 2),
        ("ABCD", 2, 3),
        ("ABCD", 3, 4),
        ("ABCD", 4, 4),
        
        # Two characters
        ("ABABAB", 0, 1),
        ("ABABAB", 1, 3),
        ("ABABAB", 2, 5),
        ("ABABAB", 3, 6),
        ("ABABAB", 4, 6),
        
        # Three characters
        ("ABCABC", 0, 1),
        ("ABCABC", 1, 2),
        ("ABCABC", 2, 4),
        ("ABCABC", 3, 6),
        ("ABCABC", 4, 6),
        
        # Long strings
        ("A" * 100, 0, 100),
        ("A" * 100, 1, 100),
        ("A" * 100, 10, 100),
        ("A" * 100, 50, 100),
        ("A" * 100, 100, 100),
        
        # Mixed patterns
        ("AABBBCCCC", 0, 4),
        ("AABBBCCCC", 1, 5),
        ("AABBBCCCC", 2, 6),
        ("AABBBCCCC", 3, 7),
        ("AABBBCCCC", 4, 8),
        ("AABBBCCCC", 5, 9),
        
        # Complex patterns
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 0, 1),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1, 2),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 2, 3),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 10, 11),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 25, 26),
        ("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 26, 26),
        
        # Repeated patterns
        ("ABCABCABC", 0, 1),
        ("ABCABCABC", 1, 2),
        ("ABCABCABC", 2, 4),
        ("ABCABCABC", 3, 6),
        ("ABCABCABC", 4, 7),
        ("ABCABCABC", 5, 8),
        ("ABCABCABC", 6, 9),
        
        # Edge cases with k
        ("AABABBA", 0, 2),
        ("AABABBA", 1, 4),
        ("AABABBA", 2, 5),
        ("AABABBA", 3, 6),
        ("AABABBA", 4, 7),
        ("AABABBA", 5, 7),
        ("AABABBA", 6, 7),
        ("AABABBA", 7, 7),
        ("AABABBA", 8, 7),
        ("AABABBA", 100, 7),
        
        # Special characters
        ("!@#$%^&*()", 0, 1),
        ("!@#$%^&*()", 1, 2),
        ("!@#$%^&*()", 2, 3),
        ("!@#$%^&*()", 5, 6),
        ("!@#$%^&*()", 9, 10),
        ("!@#$%^&*()", 10, 10),
        
        # Numbers
        ("123456789", 0, 1),
        ("123456789", 1, 2),
        ("123456789", 2, 3),
        ("123456789", 5, 6),
        ("123456789", 8, 9),
        ("123456789", 9, 9),
        
        # Mixed alphanumeric
        ("A1B2C3D4E5", 0, 1),
        ("A1B2C3D4E5", 1, 2),
        ("A1B2C3D4E5", 2, 3),
        ("A1B2C3D4E5", 5, 6),
        ("A1B2C3D4E5", 9, 10),
        ("A1B2C3D4E5", 10, 10),
    ]
    
    print("Testing Longest Repeating Character Replacement solution...")
    for i, (s, k, expected) in enumerate(test_cases):
        result = characterReplacement(s, k)
        if result == expected:
            print(f"✓ Test {i+1} passed: s='{s}', k={k}, result={result}")
        else:
            print(f"✗ Test {i+1} failed: s='{s}', k={k}")
            print(f"  Expected: {expected}, Got: {result}")
    
    print("\nAll tests completed!")


# Performance test
def test_performance():
    """Test solution performance with large input"""
    import time
    import random
    import string
    
    # Generate large string
    chars = string.ascii_uppercase
    large_s = ''.join(random.choices(chars, k=10000))
    k = 100
    
    start_time = time.time()
    result = characterReplacement(large_s, k)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large string (10,000 chars) with k={k}: {end_time - start_time:.4f} seconds")
    print(f"Result: {result}")


if __name__ == "__main__":
    test_longest_repeating_character_replacement()
    test_performance()
