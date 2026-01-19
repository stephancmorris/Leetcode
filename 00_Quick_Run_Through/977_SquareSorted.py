class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        answer = collections.deque()
        l, r = 0, len(nums) - 1
        while l <= r:
            leftv, rightv = abs(nums[l]), abs(nums[r])
            if leftv > rightv:
                answer.appendleft(leftv * leftv)
                l += 1
            else: 
                answer.appendleft(rightv * rightv)
                r -= 1
        return list(answer)