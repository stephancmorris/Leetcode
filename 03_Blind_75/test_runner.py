#!/usr/bin/env python3
"""
Blind 75 Test Runner
Run this script to test all your Blind 75 solutions
"""

import os
import sys
import importlib.util
import time
from pathlib import Path

def run_tests_for_file(file_path):
    """Run tests for a specific problem file"""
    try:
        # Load the module
        spec = importlib.util.spec_from_file_location("problem", file_path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Check if the file has test functions
        if hasattr(module, 'test_two_sum') or hasattr(module, 'test_contains_duplicate') or hasattr(module, 'test_max_profit'):
            print(f"\n{'='*50}")
            print(f"Testing: {os.path.basename(file_path)}")
            print(f"{'='*50}")
            
            # Run the test function
            for attr_name in dir(module):
                if attr_name.startswith('test_'):
                    test_func = getattr(module, attr_name)
                    if callable(test_func):
                        try:
                            test_func()
                        except Exception as e:
                            print(f"Error running {attr_name}: {e}")
        else:
            print(f"Skipping {os.path.basename(file_path)} - no test functions found")
            
    except Exception as e:
        print(f"Error loading {file_path}: {e}")

def run_all_tests():
    """Run tests for all Blind 75 problems"""
    print("Blind 75 Test Runner")
    print("=" * 50)
    
    # Define directories to check
    directories = [
        "03_Blind_75/Easy",
        "03_Blind_75/Medium", 
        "03_Blind_75/Hard"
    ]
    
    total_files = 0
    tested_files = 0
    
    for directory in directories:
        if os.path.exists(directory):
            print(f"\nChecking directory: {directory}")
            python_files = [f for f in os.listdir(directory) if f.endswith('.py')]
            total_files += len(python_files)
            
            for file in sorted(python_files):
                file_path = os.path.join(directory, file)
                run_tests_for_file(file_path)
                tested_files += 1
    
    print(f"\n{'='*50}")
    print(f"Test Summary: {tested_files}/{total_files} files processed")
    print(f"{'='*50}")

def run_specific_test(file_name):
    """Run tests for a specific file"""
    directories = [
        "03_Blind_75/Easy",
        "03_Blind_75/Medium", 
        "03_Blind_75/Hard"
    ]
    
    for directory in directories:
        if os.path.exists(directory):
            file_path = os.path.join(directory, file_name)
            if os.path.exists(file_path):
                run_tests_for_file(file_path)
                return
    
    print(f"File {file_name} not found in Blind 75 directories")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Run specific file
        file_name = sys.argv[1]
        if not file_name.endswith('.py'):
            file_name += '.py'
        run_specific_test(file_name)
    else:
        # Run all tests
        run_all_tests()
