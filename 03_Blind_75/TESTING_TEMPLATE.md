# Testing Template for Blind 75 Problems

## Quick Testing Template

Copy this template into each of your Blind 75 problem files:

```python
# Add this to the end of your problem file

# Test cases
def test_solution():
    """Test cases for [Problem Name]"""
    test_cases = [
        # Basic test cases
        # (input_params, expected_output),
        
        # Edge cases
        # (input_params, expected_output),
        
        # LeetCode test cases
        # (input_params, expected_output),
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


# Performance test (optional)
def test_performance():
    """Test solution performance with large input"""
    import time
    import random
    
    # Generate large test case
    large_input = generate_large_test_case()  # You define this
    
    start_time = time.time()
    result = your_function_name(large_input)
    end_time = time.time()
    
    print(f"\nPerformance Test:")
    print(f"Large input: {end_time - start_time:.4f} seconds")
    print(f"Result: {result}")


if __name__ == "__main__":
    test_solution()
    # test_performance()  # Uncomment if you want performance testing
```

## How to Use the Testing System

### 1. Individual File Testing
```bash
# Test a specific file
python3 01_Two_Sum.py

# Or use the test runner
python3 test_runner.py 01_Two_Sum.py
```

### 2. Test All Files
```bash
# Run all tests
python3 test_runner.py
```

### 3. Add Tests to Each Problem

For each problem, add test cases like this:

**Example for Contains Duplicate:**
```python
def test_contains_duplicate():
    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        ([1, 1, 1, 3, 3, 4, 3, 2, 4, 2], True),
        ([1], False),
        ([], False),
    ]
    
    print("Testing Contains Duplicate solution...")
    for i, (nums, expected) in enumerate(test_cases):
        result = containsDuplicate(nums)
        if result == expected:
            print(f"✓ Test {i+1} passed: nums={nums}, result={result}")
        else:
            print(f"✗ Test {i+1} failed: nums={nums}")
            print(f"  Expected: {expected}, Got: {result}")
    
    print("\nAll tests completed!")
```

**Example for Valid Anagram:**
```python
def test_valid_anagram():
    test_cases = [
        ("anagram", "nagaram", True),
        ("rat", "car", False),
        ("a", "ab", False),
        ("", "", True),
        ("a", "a", True),
    ]
    
    print("Testing Valid Anagram solution...")
    for i, (s, t, expected) in enumerate(test_cases):
        result = isAnagram(s, t)
        if result == expected:
            print(f"✓ Test {i+1} passed: s='{s}', t='{t}', result={result}")
        else:
            print(f"✗ Test {i+1} failed: s='{s}', t='{t}'")
            print(f"  Expected: {expected}, Got: {result}")
    
    print("\nAll tests completed!")
```

## Testing Best Practices

### 1. Test Categories
- **Basic Cases**: Normal, expected inputs
- **Edge Cases**: Empty inputs, single elements, boundary values
- **LeetCode Cases**: Exact test cases from LeetCode
- **Performance Cases**: Large inputs to verify time complexity

### 2. Test Data
- **Realistic Data**: Use realistic test data
- **Boundary Values**: Test at the limits of constraints
- **Edge Cases**: Empty arrays, single elements, duplicates
- **Error Cases**: Invalid inputs (if applicable)

### 3. Assertions
- **Clear Messages**: Helpful error messages
- **Expected vs Actual**: Show both values when tests fail
- **Multiple Checks**: Test different aspects of the solution

### 4. Performance Testing
- **Large Inputs**: Test with maximum constraint sizes
- **Time Measurement**: Measure execution time
- **Memory Usage**: Check memory consumption if needed
- **Scalability**: Verify O(n) or O(log n) behavior

## Common Test Patterns

### Arrays
```python
# Empty array
([], expected_result)

# Single element
([1], expected_result)

# Two elements
([1, 2], expected_result)

# All same elements
([1, 1, 1], expected_result)

# Negative numbers
([-1, -2, -3], expected_result)
```

### Strings
```python
# Empty string
("", expected_result)

# Single character
("a", expected_result)

# Two characters
("ab", expected_result)

# All same characters
("aaa", expected_result)

# Mixed case
("Aa", expected_result)
```

### Trees
```python
# Empty tree
(None, expected_result)

# Single node
(TreeNode(1), expected_result)

# Two nodes
(TreeNode(1, TreeNode(2)), expected_result)

# Balanced tree
(TreeNode(3, TreeNode(9), TreeNode(20)), expected_result)
```

## Debugging Failed Tests

### 1. Add Debug Prints
```python
def your_function(params):
    # Add debug prints
    print(f"Debug: input = {params}")
    
    # Your solution
    result = ...
    
    print(f"Debug: result = {result}")
    return result
```

### 2. Step-by-Step Debugging
```python
def debug_test():
    """Debug a specific test case"""
    input_params = [2, 7, 11, 15]
    target = 9
    
    print(f"Input: {input_params}")
    print(f"Target: {target}")
    
    result = twoSum(input_params, target)
    print(f"Result: {result}")
    
    # Add more debug information as needed
```

### 3. Compare with Expected
```python
def compare_results():
    """Compare your result with expected"""
    input_params = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]
    
    result = twoSum(input_params, target)
    
    print(f"Input: {input_params}, Target: {target}")
    print(f"Expected: {expected}")
    print(f"Actual: {result}")
    print(f"Match: {result == expected}")
```

This testing system will help you:
1. **Verify correctness** of your solutions
2. **Catch bugs** early
3. **Test edge cases** you might miss
4. **Build confidence** in your implementations
5. **Prepare for interviews** with tested solutions
