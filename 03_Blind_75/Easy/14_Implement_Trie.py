"""
LeetCode 208. Implement Trie (Prefix Tree)
Difficulty: Easy
Category: Tries

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently 
store and search strings in a dataset of strings. There are various applications of this 
data structure, such as autocomplete and spellchecker.

Implement the Trie class:
- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Time Complexity: O(m) for each operation where m is length of word
Space Complexity: O(ALPHABET_SIZE * N * M) where N is number of words, M is average length
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # TODO: Implement your solution here
        pass

    def insert(self, word):
        """
        Inserts a word into the trie.
        
        Args:
            word: String to insert
        """
        # TODO: Implement your solution here
        pass

    def search(self, word):
        """
        Returns if the word is in the trie.
        
        Args:
            word: String to search for
            
        Returns:
            Boolean indicating if word exists in trie
        """
        # TODO: Implement your solution here
        pass

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        
        Args:
            prefix: Prefix to search for
            
        Returns:
            Boolean indicating if any word starts with prefix
        """
        # TODO: Implement your solution here
        pass
