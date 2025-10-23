"""
LeetCode 242. Valid Anagram
Difficulty: Easy
Category: Arrays & Hashing

Given two strings s and t, return true if t is an anagram of s, and false otherwise.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Time Complexity: O(n)
Space Complexity: O(1) - at most 26 characters
"""

def isAnagram(s, t):
    """
    Check if two strings are anagrams.
    
    Args:
        s: First string
        t: Second string
        
    Returns:
        Boolean indicating if strings are anagrams
    """
    # TODO: Implement your solution here
    pass


# Test cases
def test_valid_anagram():
    """Test cases for Valid Anagram"""
    test_cases = [
        # Basic test cases
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        
        # Edge cases
        ("a", "ab", False),
        ("ab", "a", False),
        ("", "", True),
        ("a", "a", True),
        ("a", "b", False),
        
        # LeetCode test cases
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        
        # Additional edge cases
        ("listen", "silent", True),
        ("hello", "world", False),
        ("abc", "cba", True),
        ("abc", "def", False),
        ("aabbcc", "abcabc", True),
        ("aabbcc", "aabbcd", False),
        
        # Case sensitivity (assuming lowercase only)
        ("A", "a", False),  # Different cases
        ("ab", "AB", False),  # Different cases
        
        # Special characters
        ("a!b", "b!a", True),
        ("a b", "b a", True),
        ("a1b", "b1a", True),
    ]
    
    print("Testing Valid Anagram solution...")
    for i, (s, t, expected) in enumerate(test_cases):
        result = isAnagram(s, t)
        if result == expected:
            print(f"✓ Test {i+1} passed: s='{s}', t='{t}', result={result}")
        else:
            print(f"✗ Test {i+1} failed: s='{s}', t='{t}'")
            print(f"  Expected: {expected}, Got: {result}")
    
    print("\nAll tests completed!")


# Performance test
def test_performance():
    """Test solution performance with large input"""
    import time
    
    # Generate large strings
    s = "a" * 1000 + "b" * 1000
    t = "b" * 1000 + "a" * 1000
    
    start_time = time.time()
    result = isAnagram(s, t)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large strings (2000 chars each): {end_time - start_time:.4f} seconds")
    print(f"Result: {result}")


if __name__ == "__main__":
    test_valid_anagram()
    test_performance()
