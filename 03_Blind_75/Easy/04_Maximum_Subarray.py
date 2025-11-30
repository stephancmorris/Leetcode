"""
LeetCode 53. Maximum Subarray
Difficulty: Easy
Category: Arrays & Hashing

Given an integer array nums, find the contiguous subarray (containing at least one number) 
which has the largest sum and return its sum.
A subarray is a contiguous part of an array.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def maxSubArray(nums):
    """
    Find the maximum sum of any contiguous subarray.
    
    Args:
        nums: Array of integers
        
    Returns:
        Maximum sum of contiguous subarray
    """
    # TODO: Implement your solution here
    # Solution 1: Sliding Window 
    # Space and time complexity: O(n)
    max_sum = float('-inf')
    current_sum = 0
    for num in nums:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
    
    # Solution 2: Without max()
    # Space and time complexity: O(n)
    # max_sum = float('-inf')
    # current_sum = 0
    # for num in nums:
    #     current_sum = current_sum + num
    #     if current_sum > max_sum:
    #         max_sum = current_sum
    # return max_sum 


# LeetCode 53. Maximum Subarray Test cases to verify the solution
def test_maxSubArray():
    assert maxSubArray([1, 2, 3, 4, 5]) == 15
    assert maxSubArray([1, 3, 4, 5]) == 13
    assert maxSubArray([1, 2, 3, 4, 5]) == 15
    assert maxSubArray([1, 2, 3, 4, 5]) == 15
    #negative numbers
    assert maxSubArray([-1, -2, -3, -4, -5]) == -1
    assert maxSubArray([-1, -2, -3, -4, -5]) == -1
    assert maxSubArray([-1, -2, -3, -4, -5]) == -1
    # Print if test cases are passed
    print("All test cases passed")

#Performance test
def test_performance():
    """Test solution performance with large input"""
    import time
    nums = [1] * 1000000
    start_time = time.time()
    result = maxSubArray(nums)
    end_time = time.time()
    print(f"Performance Test: {end_time - start_time:.4f} seconds")
    print(f"Result: {result}")

if __name__ == "__main__":
    test_maxSubArray()
    test_performance()
