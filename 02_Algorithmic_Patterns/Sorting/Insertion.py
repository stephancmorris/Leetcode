# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key # An integer key for sorting
#         self.value = value # A string value associated with the key

# This class contains the method insertionSort to sort Pair objects.
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        n = len(pairs)   # Get the length of the list
        res = []         # List to store the intermediate states of the array

# This method sorts a list of Pair objects using the Insertion Sort algorithm.
        for i in range(n):
            j = i - 1  # Start comparing from the element before the current one

            # Move elements that are greater than the current key one position ahead
            while j >= 0 and pairs[j].key > pairs[j + 1].key:
                pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]  # Swap elements
                j -= 1  # Move to the previous element

            # Clone and save the entire state of the array at this point
            res.append(pairs[:])  # Append a copy of the current state of pairs

        return res
    
#     Explanation of Insertion Sort
# Core Idea: Insertion Sort works by building a sorted subarray at the beginning of the list. With each iteration, it takes the next element and inserts it into its correct position within the sorted subarray.
# Loop Over Elements: The outer loop iterates over all elements of the list, starting from the second element (index 1) because the first element (index 0) is considered already sorted.
# Inner Loop for Sorting: The inner loop compares each element with the elements in the sorted subarray. If an element in the sorted subarray is larger than the current element, it is moved one position ahead to make space for inserting the current element in its correct place.
# Intermediate States: After each insertion, the current state of the list is cloned and added to the res list. This gives a snapshot of the array after each step of the sorting process.
# Usefulness in LeetCode Questions
# This specific implementation is useful for understanding how Insertion Sort works and for visualizing the sorting process step by step.
# In LeetCode or other coding challenges, you might be asked to sort a custom object like Pair, and understanding how to implement and modify sorting algorithms is crucial.
# Keeping track of intermediate states is generally more educational and not typically required in standard sorting algorithm implementations. However, it could be useful in certain problems where the process of sorting, not just the final sorted result, is important.
    