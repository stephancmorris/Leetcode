# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        
        lowest = prices[0]
        for price in prices:
            if price < lowest:
                lowest = price
            res = max(res, price - lowest)
        return res


# Absolutely! The problem "Best Time to Buy and Sell Stock" is a classic LeetCode question, and it's great for understanding basic concepts in algorithms, especially related to time and space complexity.

# **Problem Description:**
# Given an array `prices` where `prices[i]` is the price of a given stock on the `i`th day, the goal is to find the maximum profit you can achieve. You can complete at most one transaction (i.e., buy one and sell one share of the stock). If you cannot achieve any profit, return 0.

# **Solution Analysis:**

# 1. **Code Overview**:
#    - The solution initializes two variables: `res` (result), which will hold the maximum profit, and `lowest`, which will hold the lowest price seen so far.
#    - It then iterates over each price in `prices`.
#    - For each price, it updates `lowest` if the current price is lower than the `lowest` price seen so far.
#    - Then, it calculates the profit (`price - lowest`) and updates `res` if this profit is greater than the current `res`.
#    - Finally, it returns `res`.

# 2. **Time Complexity**:
#    - The solution only has one loop that goes through the `prices` list once.
#    - Each operation inside the loop (comparisons, subtraction, assignment) has a constant time complexity.
#    - Therefore, the overall time complexity is **O(n)**, where `n` is the length of the `prices` list.

# 3. **Space Complexity**:
#    - The solution uses only a fixed number of extra variables (`res` and `lowest`), regardless of the input size.
#    - Thus, the space complexity is **O(1)**, which means it uses constant extra space.

# 4. **Optimization and Efficiency**:
#    - This approach is efficient because it goes through the list only once.
#    - It keeps track of the lowest price seen so far and the maximum profit that can be obtained at each step, which ensures that it finds the maximum possible profit by the end of the loop.

# 5. **Possible Improvements**:
#    - Given the nature of the problem, there is little room for optimization in terms of time complexity, as any solution will need to consider each price at least once.
#    - However, code readability and clarity can always be improved. For example, more descriptive variable names could be used.

# This breakdown should help you understand how the solution works and why it is efficient in terms of time and space complexity. Good luck with your LeetCode grinding and upcoming interviews!