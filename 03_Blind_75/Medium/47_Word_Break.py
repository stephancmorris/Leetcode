"""
LeetCode 139. Word Break
Difficulty: Medium
Category: Dynamic Programming

Given a string s and a dictionary of strings wordDict, return true if s can be segmented 
into a space-separated sequence of one or more dictionary words.
Note that the same word in the dictionary may be reused multiple times in the segmentation.

Time Complexity: O(n^3)
Space Complexity: O(n)
"""

def wordBreak(s, wordDict):
    """
    Check if string can be segmented into dictionary words.
    
    Args:
        s: Input string
        wordDict: List of valid words
        
    Returns:
        Boolean indicating if string can be segmented
    """
    # TODO: Implement your solution here
    pass


# Test cases
def test_word_break():
    """Test cases for Word Break"""
    test_cases = [
        # Basic test cases
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
        
        # Edge cases
        ("", ["a", "b"], True),  # Empty string is always true
        ("a", ["a"], True),
        ("a", ["b"], False),
        ("ab", ["a", "b"], True),
        ("ab", ["ab"], True),
        ("ab", ["c"], False),
        
        # LeetCode test cases
        ("leetcode", ["leet", "code"], True),
        ("applepenapple", ["apple", "pen"], True),
        ("catsandog", ["cats", "dog", "sand", "and", "cat"], False),
        
        # Additional test cases
        ("leetcode", ["leet", "code", "lee", "t"], True),
        ("leetcode", ["leet", "code", "lee"], False),
        ("leetcode", ["leet", "code", "t"], False),
        ("leetcode", ["leet", "code", "e"], False),
        ("leetcode", ["leet", "code", "d"], False),
        
        # Single character
        ("a", ["a"], True),
        ("a", ["b"], False),
        ("a", ["a", "b"], True),
        ("a", ["b", "c"], False),
        
        # Two characters
        ("ab", ["a", "b"], True),
        ("ab", ["ab"], True),
        ("ab", ["a"], False),
        ("ab", ["b"], False),
        ("ab", ["c"], False),
        ("ab", ["a", "c"], False),
        ("ab", ["c", "b"], False),
        
        # Three characters
        ("abc", ["a", "b", "c"], True),
        ("abc", ["ab", "c"], True),
        ("abc", ["a", "bc"], True),
        ("abc", ["abc"], True),
        ("abc", ["a", "b"], False),
        ("abc", ["ab"], False),
        ("abc", ["bc"], False),
        ("abc", ["c"], False),
        
        # Four characters
        ("abcd", ["a", "b", "c", "d"], True),
        ("abcd", ["ab", "cd"], True),
        ("abcd", ["a", "bcd"], True),
        ("abcd", ["abc", "d"], True),
        ("abcd", ["abcd"], True),
        ("abcd", ["a", "b", "c"], False),
        ("abcd", ["ab", "c"], False),
        ("abcd", ["a", "bc"], False),
        ("abcd", ["abc"], False),
        
        # Five characters
        ("abcde", ["a", "b", "c", "d", "e"], True),
        ("abcde", ["ab", "cde"], True),
        ("abcde", ["a", "bcde"], True),
        ("abcde", ["abc", "de"], True),
        ("abcde", ["abcd", "e"], True),
        ("abcde", ["abcde"], True),
        ("abcde", ["a", "b", "c", "d"], False),
        ("abcde", ["ab", "c", "d"], False),
        ("abcde", ["a", "bc", "d"], False),
        ("abcde", ["a", "b", "cd"], False),
        ("abcde", ["ab", "cd"], False),
        ("abcde", ["abc", "d"], False),
        ("abcde", ["a", "bcd"], False),
        ("abcde", ["abcd"], False),
        
        # Large strings
        ("a" * 100, ["a"], True),
        ("a" * 100, ["aa"], False),
        ("a" * 100, ["a", "aa"], True),
        ("a" * 100, ["aa", "aaa"], False),
        ("a" * 100, ["a", "aa", "aaa"], True),
        ("a" * 100, ["aa", "aaa", "aaaa"], False),
        ("a" * 100, ["a", "aa", "aaa", "aaaa"], True),
        ("a" * 100, ["aa", "aaa", "aaaa", "aaaaa"], False),
        ("a" * 100, ["a", "aa", "aaa", "aaaa", "aaaaa"], True),
        ("a" * 100, ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa"], False),
        ("a" * 100, ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa"], True),
        ("a" * 100, ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa"], False),
        ("a" * 100, ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa"], True),
        ("a" * 100, ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa"], False),
        ("a" * 100, ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa"], True),
        ("a" * 100, ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa"], False),
        ("a" * 100, ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa"], True),
        ("a" * 100, ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"], False),
        ("a" * 100, ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"], True),
        
        # Very large strings
        ("a" * 1000, ["a"], True),
        ("a" * 1000, ["aa"], False),
        ("a" * 1000, ["a", "aa"], True),
        ("a" * 1000, ["aa", "aaa"], False),
        ("a" * 1000, ["a", "aa", "aaa"], True),
        ("a" * 1000, ["aa", "aaa", "aaaa"], False),
        ("a" * 1000, ["a", "aa", "aaa", "aaaa"], True),
        ("a" * 1000, ["aa", "aaa", "aaaa", "aaaaa"], False),
        ("a" * 1000, ["a", "aa", "aaa", "aaaa", "aaaaa"], True),
        ("a" * 1000, ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa"], False),
        ("a" * 1000, ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa"], True),
        ("a" * 1000, ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa"], False),
        ("a" * 1000, ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa"], True),
        ("a" * 1000, ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa"], False),
        ("a" * 1000, ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa"], True),
        ("a" * 1000, ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa"], False),
        ("a" * 1000, ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa"], True),
        ("a" * 1000, ["aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"], False),
        ("a" * 1000, ["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"], True),
        
        # Edge cases with empty string
        ("", [], True),
        ("", ["a"], True),
        ("", ["a", "b"], True),
        ("", ["a", "b", "c"], True),
        
        # Edge cases with single character
        ("a", [], False),
        ("a", ["a"], True),
        ("a", ["b"], False),
        ("a", ["a", "b"], True),
        ("a", ["b", "c"], False),
        
        # Edge cases with two characters
        ("ab", [], False),
        ("ab", ["a"], False),
        ("ab", ["b"], False),
        ("ab", ["ab"], True),
        ("ab", ["a", "b"], True),
        ("ab", ["a", "c"], False),
        ("ab", ["c", "b"], False),
        ("ab", ["c", "d"], False),
        
        # Edge cases with three characters
        ("abc", [], False),
        ("abc", ["a"], False),
        ("abc", ["b"], False),
        ("abc", ["c"], False),
        ("abc", ["ab"], False),
        ("abc", ["bc"], False),
        ("abc", ["abc"], True),
        ("abc", ["a", "b"], False),
        ("abc", ["a", "c"], False),
        ("abc", ["b", "c"], False),
        ("abc", ["a", "b", "c"], True),
        ("abc", ["a", "bc"], True),
        ("abc", ["ab", "c"], True),
        ("abc", ["a", "b", "d"], False),
        ("abc", ["a", "d", "c"], False),
        ("abc", ["d", "b", "c"], False),
        ("abc", ["d", "e", "f"], False),
        
        # Edge cases with four characters
        ("abcd", [], False),
        ("abcd", ["a"], False),
        ("abcd", ["b"], False),
        ("abcd", ["c"], False),
        ("abcd", ["d"], False),
        ("abcd", ["ab"], False),
        ("abcd", ["bc"], False),
        ("abcd", ["cd"], False),
        ("abcd", ["abc"], False),
        ("abcd", ["bcd"], False),
        ("abcd", ["abcd"], True),
        ("abcd", ["a", "b"], False),
        ("abcd", ["a", "c"], False),
        ("abcd", ["a", "d"], False),
        ("abcd", ["b", "c"], False),
        ("abcd", ["b", "d"], False),
        ("abcd", ["c", "d"], False),
        ("abcd", ["a", "b", "c"], False),
        ("abcd", ["a", "b", "d"], False),
        ("abcd", ["a", "c", "d"], False),
        ("abcd", ["b", "c", "d"], False),
        ("abcd", ["a", "b", "c", "d"], True),
        ("abcd", ["a", "bcd"], True),
        ("abcd", ["ab", "cd"], True),
        ("abcd", ["abc", "d"], True),
        ("abcd", ["a", "b", "cd"], True),
        ("abcd", ["a", "bc", "d"], True),
        ("abcd", ["ab", "c", "d"], True),
        ("abcd", ["a", "b", "c", "e"], False),
        ("abcd", ["a", "b", "e", "d"], False),
        ("abcd", ["a", "e", "c", "d"], False),
        ("abcd", ["e", "b", "c", "d"], False),
        ("abcd", ["e", "f", "g", "h"], False),
        
        # Edge cases with five characters
        ("abcde", [], False),
        ("abcde", ["a"], False),
        ("abcde", ["b"], False),
        ("abcde", ["c"], False),
        ("abcde", ["d"], False),
        ("abcde", ["e"], False),
        ("abcde", ["ab"], False),
        ("abcde", ["bc"], False),
        ("abcde", ["cd"], False),
        ("abcde", ["de"], False),
        ("abcde", ["abc"], False),
        ("abcde", ["bcd"], False),
        ("abcde", ["cde"], False),
        ("abcde", ["abcd"], False),
        ("abcde", ["bcde"], False),
        ("abcde", ["abcde"], True),
        ("abcde", ["a", "b"], False),
        ("abcde", ["a", "c"], False),
        ("abcde", ["a", "d"], False),
        ("abcde", ["a", "e"], False),
        ("abcde", ["b", "c"], False),
        ("abcde", ["b", "d"], False),
        ("abcde", ["b", "e"], False),
        ("abcde", ["c", "d"], False),
        ("abcde", ["c", "e"], False),
        ("abcde", ["d", "e"], False),
        ("abcde", ["a", "b", "c"], False),
        ("abcde", ["a", "b", "d"], False),
        ("abcde", ["a", "b", "e"], False),
        ("abcde", ["a", "c", "d"], False),
        ("abcde", ["a", "c", "e"], False),
        ("abcde", ["a", "d", "e"], False),
        ("abcde", ["b", "c", "d"], False),
        ("abcde", ["b", "c", "e"], False),
        ("abcde", ["b", "d", "e"], False),
        ("abcde", ["c", "d", "e"], False),
        ("abcde", ["a", "b", "c", "d"], False),
        ("abcde", ["a", "b", "c", "e"], False),
        ("abcde", ["a", "b", "d", "e"], False),
        ("abcde", ["a", "c", "d", "e"], False),
        ("abcde", ["b", "c", "d", "e"], False),
        ("abcde", ["a", "b", "c", "d", "e"], True),
        ("abcde", ["a", "bcde"], True),
        ("abcde", ["ab", "cde"], True),
        ("abcde", ["abc", "de"], True),
        ("abcde", ["abcd", "e"], True),
        ("abcde", ["a", "b", "cde"], True),
        ("abcde", ["a", "bc", "de"], True),
        ("abcde", ["a", "bcd", "e"], True),
        ("abcde", ["ab", "c", "de"], True),
        ("abcde", ["ab", "cd", "e"], True),
        ("abcde", ["abc", "d", "e"], True),
        ("abcde", ["a", "b", "c", "de"], True),
        ("abcde", ["a", "b", "cd", "e"], True),
        ("abcde", ["a", "bc", "d", "e"], True),
        ("abcde", ["ab", "c", "d", "e"], True),
        ("abcde", ["a", "b", "c", "d", "f"], False),
        ("abcde", ["a", "b", "c", "f", "e"], False),
        ("abcde", ["a", "b", "f", "d", "e"], False),
        ("abcde", ["a", "f", "c", "d", "e"], False),
        ("abcde", ["f", "b", "c", "d", "e"], False),
        ("abcde", ["f", "g", "h", "i", "j"], False),
    ]
    
    print("Testing Word Break solution...")
    for i, (s, wordDict, expected) in enumerate(test_cases):
        result = wordBreak(s, wordDict)
        if result == expected:
            print(f"✓ Test {i+1} passed: s='{s}', wordDict={wordDict}, result={result}")
        else:
            print(f"✗ Test {i+1} failed: s='{s}', wordDict={wordDict}")
            print(f"  Expected: {expected}, Got: {result}")
    
    print("\nAll tests completed!")


# Performance test
def test_performance():
    """Test solution performance with large input"""
    import time
    
    # Generate large string and word dictionary
    large_s = "a" * 1000
    large_wordDict = ["a" * i for i in range(1, 11)]  # ["a", "aa", "aaa", ..., "aaaaaaaaaa"]
    
    start_time = time.time()
    result = wordBreak(large_s, large_wordDict)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large string (1,000 chars) with wordDict: {end_time - start_time:.4f} seconds")
    print(f"Result: {result}")


if __name__ == "__main__":
    test_word_break()
    test_performance()
