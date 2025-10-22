"""
LeetCode 127. Word Ladder
Difficulty: Hard
Category: Graphs

A transformation sequence from word beginWord to word endWord using a dictionary wordList is 
a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:
- Every adjacent pair of words differs by a single letter.
- Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
- sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words 
in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

Time Complexity: O(M^2 * N) where M is length of word, N is number of words
Space Complexity: O(M^2 * N)
"""

def ladderLength(beginWord, endWord, wordList):
    """
    Find shortest transformation sequence length.
    
    Args:
        beginWord: Starting word
        endWord: Target word
        wordList: Dictionary of valid words
        
    Returns:
        Length of shortest transformation sequence, 0 if impossible
    """
    # TODO: Implement your solution here
    pass
