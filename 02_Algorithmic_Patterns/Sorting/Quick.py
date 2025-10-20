# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value

# This class contains the quickSort method to sort Pair objects.
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        # Initiate the quick sort process
        self.quickSortHelper(pairs, 0, len(pairs) - 1)
        return pairs

# This method recursively sorts the parts of the array using the Quick Sort algorithm.
    def quickSortHelper(self, arr: List[Pair], s: int, e: int) -> None:
        if e - s + 1 <= 1:
            return  # Base case: return if the segment length is 1 or 0

        pivot = arr[e]  # Choose the pivot as the last element
        left = s        # Pointer to track the partitioning position

        # Partitioning: move elements smaller than pivot to the left
        for i in range(s, e):
            if arr[i].key < pivot.key:
                arr[left], arr[i] = arr[i], arr[left]  # Swap elements
                left += 1  # Move the partitioning pointer

        # Place the pivot between the left and right partitions
        arr[e], arr[left] = arr[left], pivot

        # Recursive calls to quick sort the left and right partitions
        self.quickSortHelper(arr, s, left - 1)  # Quick sort the left side
        self.quickSortHelper(arr, left + 1, e)  # Quick sort the right side

