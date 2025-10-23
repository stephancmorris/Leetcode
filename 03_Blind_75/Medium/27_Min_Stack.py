"""
LeetCode 155. Min Stack
Difficulty: Medium
Category: Stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
Implement the MinStack class:
- MinStack() initializes the stack object.
- void push(int val) pushes the element val onto the stack.
- void pop() removes the element on the top of the stack.
- int top() gets the top element of the stack.
- int getMin() retrieves the minimum element in the stack.

Time Complexity: O(1) for all operations
Space Complexity: O(n)
"""

class MinStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # TODO: Implement your solution here
        pass

    def push(self, val):
        """
        Push element onto stack.
        
        Args:
            val: Value to push
        """
        # TODO: Implement your solution here
        pass

    def pop(self):
        """
        Remove element from top of stack.
        """
        # TODO: Implement your solution here
        pass

    def top(self):
        """
        Get top element of stack.
        
        Returns:
            Top element of stack
        """
        # TODO: Implement your solution here
        pass

    def getMin(self):
        """
        Get minimum element in stack.
        
        Returns:
            Minimum element in stack
        """
        # TODO: Implement your solution here
        pass


# Test cases
def test_min_stack():
    """Test cases for Min Stack"""
    test_cases = [
        # Basic test cases
        (["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"], 
         [[], [-2], [0], [-3], [], [], [], []], 
         [None, None, None, None, -3, None, 0, -2]),
        
        # Edge cases
        (["MinStack", "push", "getMin"], [[], [1], []], [None, None, 1]),
        (["MinStack", "push", "push", "getMin", "pop", "getMin"], 
         [[], [1], [2], [], [], []], 
         [None, None, None, 1, None, 1]),
        
        # LeetCode test cases
        (["MinStack", "push", "push", "push", "getMin", "pop", "top", "getMin"], 
         [[], [-2], [0], [-3], [], [], [], []], 
         [None, None, None, None, -3, None, 0, -2]),
        
        # Additional test cases
        (["MinStack", "push", "push", "push", "push", "getMin", "pop", "getMin", "pop", "getMin"], 
         [[], [1], [2], [3], [0], [], [], [], [], []], 
         [None, None, None, None, None, 0, None, 1, None, 1]),
        
        # Single element
        (["MinStack", "push", "getMin", "top", "pop"], 
         [[], [5], [], [], []], 
         [None, None, 5, 5, None]),
        
        # Duplicate minimums
        (["MinStack", "push", "push", "push", "getMin", "pop", "getMin", "pop", "getMin"], 
         [[], [1], [1], [1], [], [], [], [], []], 
         [None, None, None, None, 1, None, 1, None, 1]),
        
        # Negative numbers
        (["MinStack", "push", "push", "push", "getMin", "pop", "getMin"], 
         [[], [-1], [-2], [-3], [], [], []], 
         [None, None, None, None, -3, None, -2]),
        
        # Large numbers
        (["MinStack", "push", "push", "getMin"], 
         [[], [1000000000], [-1000000000], []], 
         [None, None, None, -1000000000]),
    ]
    
    print("Testing Min Stack solution...")
    for i, (operations, values, expected) in enumerate(test_cases):
        stack = MinStack()
        results = []
        
        for j, op in enumerate(operations):
            if op == "MinStack":
                results.append(None)
            elif op == "push":
                stack.push(values[j][0])
                results.append(None)
            elif op == "pop":
                stack.pop()
                results.append(None)
            elif op == "top":
                result = stack.top()
                results.append(result)
            elif op == "getMin":
                result = stack.getMin()
                results.append(result)
        
        if results == expected:
            print(f"✓ Test {i+1} passed: operations={operations}")
        else:
            print(f"✗ Test {i+1} failed: operations={operations}")
            print(f"  Expected: {expected}")
            print(f"  Got: {results}")
    
    print("\nAll tests completed!")


# Performance test
def test_performance():
    """Test solution performance with large input"""
    import time
    
    stack = MinStack()
    
    # Push many elements
    start_time = time.time()
    for i in range(10000):
        stack.push(i)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Push 10,000 elements: {end_time - start_time:.4f} seconds")
    
    # Get minimum many times
    start_time = time.time()
    for i in range(1000):
        stack.getMin()
    end_time = time.time()
    
    print(f"Get minimum 1,000 times: {end_time - start_time:.4f} seconds")


if __name__ == "__main__":
    test_min_stack()
    test_performance()
