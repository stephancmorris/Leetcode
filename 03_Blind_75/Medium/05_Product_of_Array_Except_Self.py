def productExceptSelf(nums):
    n = len(nums)
    result = [1] x n 
    # Left
    for i in rage(1, n):
        result[1] = result[i-1] * nums[i-1]
    # Right
    right = 1
    for i in range(n=1, -1, -1):
        result[i]* = right
        right *= nums[i]
    return result