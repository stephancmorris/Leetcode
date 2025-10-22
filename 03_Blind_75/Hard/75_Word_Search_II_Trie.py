"""
LeetCode 212. Word Search II (Alternative Implementation)
Difficulty: Hard
Category: Backtracking

Given an m x n board of characters and a list of strings words, return all words on the board.
Each word must be constructed from letters of sequentially adjacent cells, where adjacent 
cells are horizontally or vertically neighboring. The same letter cell may not be used more 
than once in a word.

This is an alternative implementation focusing on backtracking approach with Trie optimization.

Time Complexity: O(m * n * 4^L) where L is total length of all words
Space Complexity: O(N) where N is total number of letters in all words
"""

def findWords(board, words):
    """
    Find all words that exist on the board using Trie optimization.
    
    Args:
        board: 2D grid of characters
        words: List of words to search for
        
    Returns:
        List of words found on the board
    """
    # TODO: Implement your solution here
    pass
