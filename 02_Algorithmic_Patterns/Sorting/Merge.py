# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key # The key used for sorting
#         self.value = value # The value associated with the key
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        # Initiate the merge sort process
        return self.mergeSortHelper(pairs, 0, len(pairs) - 1)

# This method recursively sorts the parts of the array.

    def mergeSortHelper(self, pairs: List[Pair], s: int, e: int) -> List[Pair]:
        if e - s + 1 <= 1:
            return pairs  # Base case: return if the segment length is 1 or 0

        m = (s + e) // 2  # Calculate the middle index

        # Recursive calls to sort the left and right halves
        self.mergeSortHelper(pairs, s, m)
        self.mergeSortHelper(pairs, m + 1, e)

        # Merge the sorted halves
        self.merge(pairs, s, m, e)
        
        return pairs

# This method merges two sorted subarrays into one.
    def merge(self, arr: List[Pair], s: int, m: int, e: int) -> None:
        # Create copies of the left and right subarrays
        L = arr[s: m + 1]
        R = arr[m + 1: e + 1]

        i, j, k = 0, 0, s

        # Merge the subarrays back into arr
        while i < len(L) and j < len(R):
            if L[i].key <= R[j].key:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # Copy the remaining elements of L, if any
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # Copy the remaining elements of R, if any
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Explanation of Merge Sort
# Divide: The array is divided into two halves (left and right), and these halves are further divided recursively until each subarray has one or no elements.
# Conquer: Each pair of subarrays is merged back together in a sorted manner, starting from the smallest subarrays (length 1 or 0) and gradually building up to the entire array.
# Combine: The merge function combines two sorted subarrays (L and R) into a single sorted array. It keeps track of three indices: i for the left subarray, j for the right subarray, and k for the main array (arr), copying the smaller element from either L or R back into arr.
# Usefulness in LeetCode Questions
# Merge Sort is a fundamental sorting algorithm and is often used in coding interviews and algorithmic challenges because of its efficiency for large datasets.
# Understanding merge sort is also crucial for grasping other divide and conquer algorithms.
# The ability to modify and adapt sorting algorithms to work with custom data structures (like Pair in this case) is a valuable skill in solving more complex problems.