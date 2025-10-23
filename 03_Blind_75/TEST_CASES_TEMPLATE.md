# Test Cases Template for All Blind 75 Problems

## How to Use This Template

For each remaining Blind 75 problem, copy the appropriate template below and customize it for that specific problem.

## Template Categories

### 1. Array/String Problems
```python
# Test cases
def test_problem_name():
    """Test cases for [Problem Name]"""
    test_cases = [
        # Basic test cases
        (input1, expected1),
        (input2, expected2),
        
        # Edge cases
        ([], expected_empty),
        ([single_element], expected_single),
        
        # LeetCode test cases
        (leetcode_input1, leetcode_expected1),
        (leetcode_input2, leetcode_expected2),
        
        # Additional test cases
        (edge_case1, expected_edge1),
        (edge_case2, expected_edge2),
    ]
    
    print("Testing [Problem Name] solution...")
    for i, (input_params, expected) in enumerate(test_cases):
        result = your_function_name(input_params)
        if result == expected:
            print(f"✓ Test {i+1} passed: input={input_params}, result={result}")
        else:
            print(f"✗ Test {i+1} failed: input={input_params}")
            print(f"  Expected: {expected}, Got: {result}")
    
    print("\nAll tests completed!")


# Performance test
def test_performance():
    """Test solution performance with large input"""
    import time
    import random
    
    # Generate large test case
    large_input = generate_large_test_case()
    
    start_time = time.time()
    result = your_function_name(large_input)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large input: {end_time - start_time:.4f} seconds")
    print(f"Result: {result}")


if __name__ == "__main__":
    test_problem_name()
    test_performance()
```

### 2. Tree Problems
```python
# Test cases
def test_problem_name():
    """Test cases for [Problem Name]"""
    test_cases = [
        # Basic test cases
        (create_tree1(), expected1),
        (create_tree2(), expected2),
        
        # Edge cases
        (None, expected_empty),
        (create_single_node(), expected_single),
        
        # LeetCode test cases
        (create_leetcode_tree1(), leetcode_expected1),
        (create_leetcode_tree2(), leetcode_expected2),
        
        # Additional test cases
        (create_edge_tree1(), expected_edge1),
        (create_edge_tree2(), expected_edge2),
    ]
    
    print("Testing [Problem Name] solution...")
    for i, (root, expected) in enumerate(test_cases):
        result = your_function_name(root)
        if result == expected:
            print(f"✓ Test {i+1} passed: result={result}")
        else:
            print(f"✗ Test {i+1} failed")
            print(f"  Expected: {expected}, Got: {result}")
    
    print("\nAll tests completed!")


# Helper functions for creating trees
def create_tree1():
    """Create test tree 1"""
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    return root

def create_tree2():
    """Create test tree 2"""
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    return root

def create_single_node():
    """Create single node tree"""
    return TreeNode(1)

def create_empty_tree():
    """Create empty tree"""
    return None


# Performance test
def test_performance():
    """Test solution performance with large tree"""
    import time
    
    # Generate large tree
    large_tree = create_large_tree()
    
    start_time = time.time()
    result = your_function_name(large_tree)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large tree: {end_time - start_time:.4f} seconds")
    print(f"Result: {result}")


if __name__ == "__main__":
    test_problem_name()
    test_performance()
```

### 3. Linked List Problems
```python
# Test cases
def test_problem_name():
    """Test cases for [Problem Name]"""
    test_cases = [
        # Basic test cases
        (create_list1(), expected1),
        (create_list2(), expected2),
        
        # Edge cases
        (None, expected_empty),
        (create_single_node(), expected_single),
        
        # LeetCode test cases
        (create_leetcode_list1(), leetcode_expected1),
        (create_leetcode_list2(), leetcode_expected2),
        
        # Additional test cases
        (create_edge_list1(), expected_edge1),
        (create_edge_list2(), expected_edge2),
    ]
    
    print("Testing [Problem Name] solution...")
    for i, (head, expected) in enumerate(test_cases):
        result = your_function_name(head)
        if result == expected:
            print(f"✓ Test {i+1} passed: result={result}")
        else:
            print(f"✗ Test {i+1} failed")
            print(f"  Expected: {expected}, Got: {result}")
    
    print("\nAll tests completed!")


# Helper functions for creating linked lists
def create_list1():
    """Create test list 1"""
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    return head

def create_list2():
    """Create test list 2"""
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    return head

def create_single_node():
    """Create single node list"""
    return ListNode(1)

def create_empty_list():
    """Create empty list"""
    return None


# Performance test
def test_performance():
    """Test solution performance with large list"""
    import time
    
    # Generate large list
    large_list = create_large_list()
    
    start_time = time.time()
    result = your_function_name(large_list)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large list: {end_time - start_time:.4f} seconds")
    print(f"Result: {result}")


if __name__ == "__main__":
    test_problem_name()
    test_performance()
```

### 4. Graph Problems
```python
# Test cases
def test_problem_name():
    """Test cases for [Problem Name]"""
    test_cases = [
        # Basic test cases
        (graph1, expected1),
        (graph2, expected2),
        
        # Edge cases
        ([], expected_empty),
        (single_node_graph, expected_single),
        
        # LeetCode test cases
        (leetcode_graph1, leetcode_expected1),
        (leetcode_graph2, leetcode_expected2),
        
        # Additional test cases
        (edge_graph1, expected_edge1),
        (edge_graph2, expected_edge2),
    ]
    
    print("Testing [Problem Name] solution...")
    for i, (graph, expected) in enumerate(test_cases):
        result = your_function_name(graph)
        if result == expected:
            print(f"✓ Test {i+1} passed: result={result}")
        else:
            print(f"✗ Test {i+1} failed")
            print(f"  Expected: {expected}, Got: {result}")
    
    print("\nAll tests completed!")


# Performance test
def test_performance():
    """Test solution performance with large graph"""
    import time
    
    # Generate large graph
    large_graph = create_large_graph()
    
    start_time = time.time()
    result = your_function_name(large_graph)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large graph: {end_time - start_time:.4f} seconds")
    print(f"Result: {result}")


if __name__ == "__main__":
    test_problem_name()
    test_performance()
```

## Specific Test Cases for Common Problems

### Maximum Subarray (Kadane's Algorithm)
```python
test_cases = [
    # Basic test cases
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1], 1),
    ([5, 4, -1, 7, 8], 23),
    
    # Edge cases
    ([-1], -1),
    ([-2, -1], -1),
    ([1, 2, 3, 4, 5], 15),
    ([-5, -4, -3, -2, -1], -1),
    
    # LeetCode test cases
    ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
    ([1], 1),
    ([5, 4, -1, 7, 8], 23),
]
```

### Best Time to Buy and Sell Stock
```python
test_cases = [
    # Basic test cases
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
    
    # Edge cases
    ([1], 0),
    ([1, 2], 1),
    ([2, 1], 0),
    ([1, 1, 1], 0),
    
    # LeetCode test cases
    ([7, 1, 5, 3, 6, 4], 5),
    ([7, 6, 4, 3, 1], 0),
]
```

### 3Sum
```python
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
    
    # LeetCode test cases
    ([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
    ([0, 1, 1], []),
    ([0, 0, 0], [[0, 0, 0]]),
]
```

### Container With Most Water
```python
test_cases = [
    # Basic test cases
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1),
    
    # Edge cases
    ([1], 0),
    ([1, 2], 1),
    ([2, 1], 1),
    ([1, 2, 1], 2),
    
    # LeetCode test cases
    ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
    ([1, 1], 1),
]
```

### Longest Substring Without Repeating Characters
```python
test_cases = [
    # Basic test cases
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
    
    # Edge cases
    ("", 0),
    ("a", 1),
    ("ab", 2),
    ("abc", 3),
    ("aab", 2),
    
    # LeetCode test cases
    ("abcabcbb", 3),
    ("bbbbb", 1),
    ("pwwkew", 3),
]
```

## Test Case Categories

### 1. Basic Test Cases
- Normal, expected inputs
- Standard LeetCode examples
- Typical use cases

### 2. Edge Cases
- Empty inputs
- Single elements
- Two elements
- All same elements
- Boundary values

### 3. LeetCode Test Cases
- Exact test cases from LeetCode
- Official examples
- Verified correct outputs

### 4. Additional Test Cases
- Negative numbers
- Large numbers
- Special characters
- Complex scenarios

### 5. Performance Test Cases
- Large inputs
- Maximum constraint values
- Time complexity verification

## Best Practices

### 1. Test Case Design
- **Coverage**: Test all code paths
- **Edge Cases**: Include boundary conditions
- **Realistic Data**: Use realistic test data
- **Performance**: Test with large inputs

### 2. Assertion Strategy
- **Clear Messages**: Helpful error messages
- **Expected vs Actual**: Show both values
- **Multiple Checks**: Test different aspects

### 3. Performance Testing
- **Large Inputs**: Test with maximum constraints
- **Time Measurement**: Measure execution time
- **Memory Usage**: Check memory consumption
- **Scalability**: Verify time complexity

### 4. Debugging Failed Tests
- **Add Debug Prints**: Show intermediate values
- **Step-by-Step**: Trace through execution
- **Compare Results**: Compare with expected output

## Quick Reference

### Common Test Patterns
```python
# Empty input
([], expected_empty)

# Single element
([single_element], expected_single)

# Two elements
([elem1, elem2], expected_two)

# All same elements
([same, same, same], expected_same)

# Negative numbers
([-1, -2, -3], expected_negative)

# Large numbers
([1000000000, 2000000000], expected_large)
```

### Performance Test Patterns
```python
# Large array
large_input = list(range(1, 10001))

# Large string
large_string = "a" * 10000

# Large tree
large_tree = create_tree_with_depth(10)

# Large graph
large_graph = create_graph_with_nodes(1000)
```

This template provides everything you need to add comprehensive test cases to all remaining Blind 75 problems!
