class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # nums.sort()

        # print(nums)

        # for i, v in enumerate(nums):
        #     if i != v:
        #         return i 

        
        #     if v == len(nums) - 1:
        #         return v + 1

        return sum(range(len(nums)+1)) - sum(nums)
        