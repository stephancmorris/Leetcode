# Given a string s, find the length of the longest 
# substring
#  without repeating characters.

 

# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)
        return res


# Certainly! The problem "Length of Longest Substring Without Repeating Characters" is an excellent example to understand the sliding window technique and its application in solving string-related problems. Let's break down this solution.

# **Problem Description:**
# Given a string `s`, find the length of the longest substring without repeating characters.

# **Solution Analysis:**

# 1. **Code Overview**:
#    - The solution uses a set `charSet` to keep track of the characters in the current window (substring).
#    - Two pointers are used: `l` (left) and `r` (right). Initially, both are at the start of the string.
#    - The right pointer `r` iterates over the string.
#    - If the character at the right pointer exists in the set, it indicates a repeat, and the left pointer moves rightwards (and the corresponding character is removed from the set) until the repeat is resolved.
#    - Each time a new character is added to the set, the result `res` is updated with the length of the current window if it is greater than the previous result.
#    - The function returns the maximum length found (`res`).

# 2. **Time Complexity**:
#    - The right pointer `r` traverses each character in the string once, giving a complexity of O(n).
#    - The left pointer `l` moves only when a repeating character is found, and in total, it can move across each character at most once. Thus, it also contributes O(n) over the entire run.
#    - Combining these, the overall time complexity is **O(n)**, where `n` is the length of the string `s`.

# 3. **Space Complexity**:
#    - The additional space used is for the set `charSet`, which in the worst case, can store all unique characters of the string.
#    - Thus, the space complexity is **O(min(m, n))**, where `m` is the size of the character set (the number of unique characters possible) and `n` is the length of the string.

# 4. **Comments on Code**:
#    - `charSet` is used to store characters in the current window without repeats.
#    - `l` and `r` are pointers to denote the current window's start and end.
#    - The `while` loop inside the `for` loop is used to move the left pointer forward to ensure no repeats in the current window.
#    - The maximum length of the substring is continuously updated in `res`.
#    - This code efficiently handles the substring search using the sliding window technique, which is optimal for such problems.

# This breakdown should provide a clear understanding of how the sliding window technique is applied in this problem and its efficiency in terms of time and space complexity. This understanding will be beneficial for your LeetCode preparation and job interviews. Good luck!