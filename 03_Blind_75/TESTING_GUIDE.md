# Testing Your Blind 75 Solutions

## Testing Approaches

### 1. Manual Testing with Print Statements
Add test cases directly in your solution files:

```python
def twoSum(nums, target):
    # Your solution here
    pass

# Test cases
if __name__ == "__main__":
    # Test case 1: Basic example
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = twoSum(nums1, target1)
    print(f"Test 1: {result1}")  # Expected: [0, 1]
    
    # Test case 2: Edge case
    nums2 = [3, 3]
    target2 = 6
    result2 = twoSum(nums2, target2)
    print(f"Test 2: {result2}")  # Expected: [0, 1]
    
    # Test case 3: No solution (shouldn't happen per problem constraints)
    nums3 = [1, 2, 3]
    target3 = 7
    result3 = twoSum(nums3, target3)
    print(f"Test 3: {result3}")  # Expected: []
```

### 2. Using Python's unittest Framework
Create comprehensive test suites:

```python
import unittest

class TestTwoSum(unittest.TestCase):
    def test_basic_case(self):
        nums = [2, 7, 11, 15]
        target = 9
        result = twoSum(nums, target)
        self.assertEqual(result, [0, 1])
    
    def test_duplicate_elements(self):
        nums = [3, 3]
        target = 6
        result = twoSum(nums, target)
        self.assertEqual(result, [0, 1])
    
    def test_negative_numbers(self):
        nums = [-1, -2, -3, -4, -5]
        target = -8
        result = twoSum(nums, target)
        self.assertEqual(result, [2, 4])
    
    def test_single_element(self):
        nums = [5]
        target = 5
        result = twoSum(nums, target)
        self.assertEqual(result, [])

if __name__ == "__main__":
    unittest.main()
```

### 3. Using pytest (Recommended)
More concise and powerful testing:

```python
import pytest

def test_two_sum_basic():
    assert twoSum([2, 7, 11, 15], 9) == [0, 1]

def test_two_sum_duplicates():
    assert twoSum([3, 3], 6) == [0, 1]

def test_two_sum_negative():
    assert twoSum([-1, -2, -3, -4, -5], -8) == [2, 4]

def test_two_sum_edge_cases():
    assert twoSum([1, 2], 3) == [0, 1]
    assert twoSum([1, 2, 3], 4) == [0, 2]
```

### 4. LeetCode-Style Testing
Test with LeetCode's exact test cases:

```python
def test_leetcode_cases():
    # LeetCode test cases for Two Sum
    test_cases = [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ]
    
    for nums, target, expected in test_cases:
        result = twoSum(nums, target)
        assert result == expected, f"Failed for nums={nums}, target={target}"
        print(f"✓ Passed: nums={nums}, target={target}, result={result}")
```

## Testing Strategy by Problem Type

### Arrays & Hashing Problems
```python
def test_contains_duplicate():
    # Test cases for Contains Duplicate
    assert containsDuplicate([1, 2, 3, 1]) == True
    assert containsDuplicate([1, 2, 3, 4]) == False
    assert containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]) == True
    assert containsDuplicate([1]) == False
    assert containsDuplicate([]) == False
```

### Two Pointers Problems
```python
def test_valid_palindrome():
    # Test cases for Valid Palindrome
    assert isPalindrome("A man, a plan, a canal: Panama") == True
    assert isPalindrome("race a car") == False
    assert isPalindrome(" ") == True
    assert isPalindrome("") == True
    assert isPalindrome("a") == True
```

### Tree Problems
```python
def test_max_depth():
    # Test cases for Maximum Depth of Binary Tree
    # You'll need to create tree nodes
    root1 = TreeNode(3)
    root1.left = TreeNode(9)
    root1.right = TreeNode(20)
    root1.right.left = TreeNode(15)
    root1.right.right = TreeNode(7)
    assert maxDepth(root1) == 3
    
    root2 = TreeNode(1)
    root2.right = TreeNode(2)
    assert maxDepth(root2) == 2
```

## Automated Testing Setup

### 1. Create a Test Runner Script
```python
# test_runner.py
import os
import sys
import importlib.util

def run_tests_for_file(file_path):
    """Run tests for a specific problem file"""
    try:
        spec = importlib.util.spec_from_file_location("problem", file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Run tests if they exist
        if hasattr(module, 'test_cases'):
            print(f"Running tests for {file_path}")
            for i, test_case in enumerate(module.test_cases):
                try:
                    result = module.main_function(*test_case['input'])
                    assert result == test_case['expected'], f"Test {i+1} failed"
                    print(f"  ✓ Test {i+1} passed")
                except Exception as e:
                    print(f"  ✗ Test {i+1} failed: {e}")
    except Exception as e:
        print(f"Error running tests for {file_path}: {e}")

def run_all_tests():
    """Run tests for all Blind 75 problems"""
    easy_dir = "03_Blind_75/Easy"
    medium_dir = "03_Blind_75/Medium"
    hard_dir = "03_Blind_75/Hard"
    
    for directory in [easy_dir, medium_dir, hard_dir]:
        if os.path.exists(directory):
            for file in os.listdir(directory):
                if file.endswith('.py'):
                    run_tests_for_file(os.path.join(directory, file))

if __name__ == "__main__":
    run_all_tests()
```

### 2. Add Test Cases to Each Problem
```python
# Example: 01_Two_Sum.py
def twoSum(nums, target):
    # Your solution here
    pass

# Test cases
test_cases = [
    {"input": ([2, 7, 11, 15], 9), "expected": [0, 1]},
    {"input": ([3, 2, 4], 6), "expected": [1, 2]},
    {"input": ([3, 3], 6), "expected": [0, 1]},
]

# Make the main function available for testing
main_function = twoSum

if __name__ == "__main__":
    for i, test_case in enumerate(test_cases):
        result = twoSum(*test_case["input"])
        print(f"Test {i+1}: {result == test_case['expected']}")
```

## Performance Testing

### 1. Time Complexity Testing
```python
import time
import random

def test_performance():
    """Test solution performance with large inputs"""
    # Generate large test case
    large_nums = [random.randint(1, 1000) for _ in range(10000)]
    target = 1999
    
    start_time = time.time()
    result = twoSum(large_nums, target)
    end_time = time.time()
    
    print(f"Large input (10,000 elements): {end_time - start_time:.4f} seconds")
    print(f"Result: {result}")
```

### 2. Memory Usage Testing
```python
import tracemalloc

def test_memory_usage():
    """Test memory usage of solution"""
    tracemalloc.start()
    
    # Run your solution
    nums = [random.randint(1, 1000) for _ in range(10000)]
    result = twoSum(nums, 1999)
    
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    print(f"Current memory usage: {current / 1024 / 1024:.2f} MB")
    print(f"Peak memory usage: {peak / 1024 / 1024:.2f} MB")
```

## Edge Case Testing

### 1. Common Edge Cases
```python
def test_edge_cases():
    """Test common edge cases"""
    # Empty input
    assert twoSum([], 0) == []
    
    # Single element
    assert twoSum([5], 5) == []
    
    # All same elements
    assert twoSum([1, 1, 1], 2) == [0, 1]
    
    # Negative numbers
    assert twoSum([-1, -2, -3], -5) == [1, 2]
    
    # Large numbers
    assert twoSum([1000000000, 1000000000], 2000000000) == [0, 1]
```

### 2. Boundary Testing
```python
def test_boundaries():
    """Test boundary conditions"""
    # Minimum valid input
    assert twoSum([1, 2], 3) == [0, 1]
    
    # Maximum constraint values (if specified in problem)
    # Test with arrays at the upper limit of constraints
    pass
```

## Continuous Testing

### 1. GitHub Actions (if using Git)
```yaml
# .github/workflows/test.yml
name: Test Blind 75 Solutions

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v2
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install dependencies
      run: pip install pytest
    - name: Run tests
      run: python test_runner.py
```

### 2. Local Testing Script
```python
# run_tests.py
import subprocess
import sys

def run_pytest():
    """Run pytest on all test files"""
    try:
        result = subprocess.run([sys.executable, "-m", "pytest", "-v"], 
                              capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print("Errors:", result.stderr)
        return result.returncode == 0
    except Exception as e:
        print(f"Error running pytest: {e}")
        return False

if __name__ == "__main__":
    success = run_pytest()
    sys.exit(0 if success else 1)
```

## Testing Best Practices

### 1. Test Coverage
- **Happy Path**: Normal, expected inputs
- **Edge Cases**: Empty inputs, single elements, boundary values
- **Error Cases**: Invalid inputs (if applicable)
- **Performance**: Large inputs to verify time complexity

### 2. Test Organization
- **Group Related Tests**: Test similar scenarios together
- **Clear Test Names**: Descriptive test function names
- **Assertion Messages**: Helpful error messages
- **Test Data**: Use realistic test data

### 3. Debugging Failed Tests
```python
def debug_test():
    """Debug a failing test case"""
    nums = [2, 7, 11, 15]
    target = 9
    expected = [0, 1]
    
    result = twoSum(nums, target)
    
    print(f"Input: nums={nums}, target={target}")
    print(f"Expected: {expected}")
    print(f"Actual: {result}")
    print(f"Match: {result == expected}")
    
    # Add debugging prints in your solution
    # print(f"Debug: current state = {current_state}")
```

## Quick Testing Template

Here's a template you can copy into each problem file:

```python
def your_solution_function(params):
    # TODO: Implement your solution here
    pass

# Test cases
def test_solution():
    test_cases = [
        # Add your test cases here
        # Format: (input_params, expected_output)
    ]
    
    for i, (input_params, expected) in enumerate(test_cases):
        result = your_solution_function(input_params)
        assert result == expected, f"Test {i+1} failed: expected {expected}, got {result}"
        print(f"✓ Test {i+1} passed")

if __name__ == "__main__":
    test_solution()
```

This comprehensive testing approach will help you:
1. **Verify correctness** of your solutions
2. **Catch edge cases** you might have missed
3. **Ensure performance** meets requirements
4. **Build confidence** in your implementations
5. **Prepare for interviews** with tested solutions
