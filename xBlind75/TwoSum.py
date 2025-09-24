def twoSum(nums, target):
    seen = {} # Price tag -> aisle number 
    for i, num in enumerate(nums):
        need = target - num
        if need in seen:
            return [seen[need], i]
        seen[num] = i

