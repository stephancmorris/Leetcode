"""
LeetCode 15. 3Sum
Difficulty: Medium
Category: Arrays & Hashing

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that 
i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.

Time Complexity: O(n^2)
Space Complexity: O(1) excluding output
"""

def threeSum(nums):
    """
    Find all unique triplets that sum to zero.
    
    Args:
        nums: Array of integers
        
    Returns:
        List of unique triplets that sum to zero
    """
    # TODO: Implement your solution here
    result = []
    nums.sort()

    for i,v in enumerate(nums):
        
        if (i > 0) & (v == nums[i-1]): #moves the index and skips duplicates
            continue 

        left_pointer = (i + 1)
        right_pointer = (len(nums) - 1)

        while left_pointer < right_pointer:
            currentSum = v + nums[left_pointer] + nums[right_pointer]

            if currentSum > 0:
                right_pointer -= 1

            elif currentSum < 0:
                left_pointer += 1

            else: 
                result.append([v, nums[left_pointer], nums[right_pointer]])
                left += 1
                
                #continue with an additional while loop to evaluate more solutions
            
        
    return result 


# Test cases
def test_three_sum():
    """Test cases for 3Sum"""
    test_cases = [
        # Basic test cases
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        
        # Edge cases
        ([], []),
        ([0], []),
        ([0, 0], []),
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([1, 2, 3], []),
        ([-1, 0, 1], [[-1, 0, 1]]),
        
        # LeetCode test cases
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([0, 1, 1], []),
        ([0, 0, 0], [[0, 0, 0]]),
        
        # Additional test cases
        ([-2, 0, 1, 1, 2], [[-2, 0, 2], [-2, 1, 1]]),
        ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
        ([1, 2, -2, -1], []),
        ([-1, 0, 1, 0], [[-1, 0, 1]]),
        
        # Duplicates
        ([0, 0, 0, 0], [[0, 0, 0]]),
        ([1, 1, -2], [[1, 1, -2]]),
        ([-1, -1, 2], [[-1, -1, 2]]),
        
        # Large numbers
        ([1000000000, -1000000000, 0], [[-1000000000, 0, 1000000000]]),
        
        # Negative numbers
        ([-1, -2, -3, 6], [[-1, -2, 3]]),
        ([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6], [[-4, -2, 6], [-4, 0, 4], [-4, 1, 3], [-4, 2, 2], [-2, -2, 4], [-2, 0, 2]]),
    ]
    
    print("Testing 3Sum solution...")
    for i, (nums, expected) in enumerate(test_cases):
        result = threeSum(nums)
        # Sort each triplet and the overall result for comparison
        result_sorted = [sorted(triplet) for triplet in result]
        result_sorted.sort()
        expected_sorted = [sorted(triplet) for triplet in expected]
        expected_sorted.sort()
        
        if result_sorted == expected_sorted:
            print(f"✓ Test {i+1} passed: nums={nums}")
            print(f"  Number of triplets: {len(result)}")
        else:
            print(f"✗ Test {i+1} failed: nums={nums}")
            print(f"  Expected {len(expected)} triplets, Got {len(result)} triplets")
            print(f"  Expected: {expected}")
            print(f"  Got: {result}")
    
    print("\nAll tests completed!")


# Performance test
def test_performance():
    """Test solution performance with large input"""
    import time
    import random
    
    # Generate large array
    large_nums = [random.randint(-1000, 1000) for _ in range(1000)]
    
    start_time = time.time()
    result = threeSum(large_nums)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large array (1,000 elements): {end_time - start_time:.4f} seconds")
    print(f"Number of triplets: {len(result)}")


if __name__ == "__main__":
    test_three_sum()
    test_performance()
