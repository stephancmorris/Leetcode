"""
LeetCode 49. Group Anagrams
Difficulty: Easy
Category: Arrays & Hashing

Given an array of strings strs, group the anagrams together. You can return the answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Time Complexity: O(n * m * log(m)) where n is number of strings, m is average length
Space Complexity: O(n * m)
"""

def groupAnagrams(strs):
    """
    Group strings that are anagrams of each other.
    
    Args:
        strs: List of strings
        
    Returns:
        List of lists, where each inner list contains anagrams
    """

    
    # Solution 1: m * n * 26 is possible using a count of each char 0-26
    # m = total number of input strings, n = avergage len of str * 26
    # Hashmap is used with pattern(char count) as key : Value = list of anagrams
    res = defaultdict(list) # mapping charcount to list of anagrams
    for s in strs: # loop through str with s being each string
        count = [0] * 26 # set to 26 char
        for c in s:
            count[ord(c) - ord('a')] += 1 # a - a = 0, map a to 0
        res[tuple(count)].append(s)

    return list(res.values())

    # Sorted Solution:
    # def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    #     res = defaultdict(list)
    #     for s in strs:
    #         count = [0] * 26
    #         for c in s:
    #             count[ord(c) - ord('a')] += 1
    #         res[tuple(count)].append(s)
    #     return list(res.values())

# Test cases
def test_group_anagrams():
    """Test cases for Group Anagrams"""
    test_cases = [
        # Basic test cases
        (["eat","tea","tan","ate","nat","bat"], [["eat","tea","ate"],["tan","nat"],["bat"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
        
        # Edge cases
        (["a", "b"], [["a"], ["b"]]),
        (["ab", "ba"], [["ab", "ba"]]),
        (["abc", "def"], [["abc"], ["def"]]),
        
        # LeetCode test cases
        (["eat","tea","tan","ate","nat","bat"], [["eat","tea","ate"],["tan","nat"],["bat"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
        
        # Additional test cases
        (["listen", "silent", "enlist"], [["listen", "silent", "enlist"]]),
        (["hello", "world"], [["hello"], ["world"]]),
        (["aabb", "abab", "bbaa"], [["aabb", "abab", "bbaa"]]),
        (["abc", "bca", "cab", "def", "fed"], [["abc", "bca", "cab"], ["def", "fed"]]),
        
        # Single character strings
        (["a", "a", "a"], [["a", "a", "a"]]),
        (["a", "b", "c"], [["a"], ["b"], ["c"]]),
        
        # Mixed lengths
        (["a", "ab", "ba"], [["a"], ["ab", "ba"]]),
    ]
    
    print("Testing Group Anagrams solution...")
    for i, (strs, expected) in enumerate(test_cases):
        result = groupAnagrams(strs)
        # Sort each group and the overall result for comparison
        result_sorted = [sorted(group) for group in result]
        result_sorted.sort()
        expected_sorted = [sorted(group) for group in expected]
        expected_sorted.sort()
        
        if result_sorted == expected_sorted:
            print(f"✓ Test {i+1} passed: strs={strs}")
            print(f"  Result: {result}")
        else:
            print(f"✗ Test {i+1} failed: strs={strs}")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")
    
    print("\nAll tests completed!")


# Performance test
def test_performance():
    """Test solution performance with large input"""
    import time
    import random
    import string
    
    # Generate large list of strings
    strs = []
    for _ in range(1000):
        # Generate random string of length 3-10
        length = random.randint(3, 10)
        s = ''.join(random.choices(string.ascii_lowercase, k=length))
        strs.append(s)
    
    start_time = time.time()
    result = groupAnagrams(strs)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large input (1000 strings): {end_time - start_time:.4f} seconds")
    print(f"Number of groups: {len(result)}")


if __name__ == "__main__":
    test_group_anagrams()
    test_performance()
