"""
LeetCode 3. Longest Substring Without Repeating Characters
Difficulty: Medium
Category: Sliding Window

Given a string s, find the length of the longest substring without repeating characters.

Time Complexity: O(n)
Space Complexity: O(min(m, n)) where m is size of charset
"""

def lengthOfLongestSubstring(s):
    """
    Find length of longest substring without repeating characters.
    
    Args:
        s: Input string
        
    Returns:
        Length of longest substring without repeating characters
    """
    # TODO: Implement your solution here
    pass


# Test cases
def test_longest_substring_without_repeating_characters():
    """Test cases for Longest Substring Without Repeating Characters"""
    test_cases = [
        # Basic test cases
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        
        # Edge cases
        ("", 0),
        ("a", 1),
        ("ab", 2),
        ("abc", 3),
        ("aab", 2),
        ("abab", 2),
        
        # LeetCode test cases
        ("abcabcbb", 3),
        ("bbbbb", 1),
        ("pwwkew", 3),
        
        # Additional test cases
        ("dvdf", 3),
        ("anviaj", 5),
        ("tmmzuxt", 5),
        ("abcdef", 6),
        ("abcdefghijklmnopqrstuvwxyz", 26),
        ("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz", 26),
        
        # Single character repeated
        ("aaaaa", 1),
        ("bbbbbb", 1),
        ("ccccccc", 1),
        
        # Two characters alternating
        ("abababab", 2),
        ("cdcdcdcd", 2),
        ("efefefef", 2),
        
        # All unique characters
        ("abcdefghijklmnopqrstuvwxyz", 26),
        ("zyxwvutsrqponmlkjihgfedcba", 26),
        
        # Mixed case
        ("AaBbCc", 6),
        ("aAbBcC", 6),
        ("ABCabc", 6),
        
        # Numbers and special characters
        ("1234567890", 10),
        ("!@#$%^&*()", 10),
        ("a1b2c3d4e5", 10),
        
        # Spaces
        ("a b c d e", 5),
        ("hello world", 5),
        ("the quick brown fox", 10),
        
        # Unicode characters
        ("你好世界", 4),
        ("αβγδε", 5),
        ("🚀🚁🚂🚃🚄", 5),
    ]
    
    print("Testing Longest Substring Without Repeating Characters solution...")
    for i, (s, expected) in enumerate(test_cases):
        result = lengthOfLongestSubstring(s)
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
    
    # Generate large string with repeated patterns
    chars = string.ascii_lowercase
    large_s = ''.join(random.choices(chars, k=10000))
    
    start_time = time.time()
    result = lengthOfLongestSubstring(large_s)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large string (10,000 chars): {end_time - start_time:.4f} seconds")
    print(f"Result: {result}")


if __name__ == "__main__":
    test_longest_substring_without_repeating_characters()
    test_performance()
