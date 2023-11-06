class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {} # Dictionary used to store the frequecy of each numner in nums
        freq = [[] for i in range(len(nums) + 1)] 

        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)

        res = [] 
        for i in range(len(freq) -1,0,1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

# Another Option if we could add libraries 

from collections import Counter
import heapq

def topKFrequent2(nums, k):
    # Step 1: Build the frequency map using Counter, which is a specialized dictionary
    frequency_map = Counter(nums)

    # Step 2: Use a heap to find the k elements with the highest frequency
    # heapq.nlargest returns the k elements with the largest values from the frequency_map
    # We use a lambda function to tell nlargest to look at the frequency values for comparison
    top_k = heapq.nlargest(k, frequency_map.keys(), key=lambda x: frequency_map[x])

    return top_k

# Example usage:
nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent2(nums, k))  # Output: [1, 2]
