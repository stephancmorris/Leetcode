class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums = set(nums)
        missingNums = []

        for i in range(1, len(nums) + 1):
            # print(i)
            if i not in set_nums:
                print(i)
                missingNums.append(i)

        return missingNums