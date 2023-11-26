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