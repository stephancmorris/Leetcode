class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        answer = collections.deque()
        l, r = 0, len(nums) - 1
        while l <= r: # while the left index is less than or equal to right index

            #Fills the deque starting from greatest to least 
            leftv, rightv = abs(nums[l]), abs(nums[r])
            if leftv > rightv:
                answer.appendleft(leftv * leftv)
                l += 1
            else: 
                answer.appendleft(rightv * rightv)
                r -= 1
        return list(answer) # returns the deque but as a list 