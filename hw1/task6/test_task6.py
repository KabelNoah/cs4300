# test_task6.py

import pytest
import task6
import os

# Define test files
test_files = ["task6_read_me.txt"]

def compute_expected_word_count(file_name):
    """Reads a file and computes the expected word count dynamically."""
    with open(file_name, "r", encoding="utf-8") as file:
        return len(file.read().split())

# Metaprogramming: Dynamically generate test cases for each file
def generate_test_function(file_name):
    """Generates a test function dynamically for pytest."""
    expected_count = compute_expected_word_count(file_name)  # Compute dynamically
    def test_func():
        assert task6.count_words_in_file(file_name) == expected_count
    test_func.__name__ = f"test_word_count_{os.path.splitext(file_name)[0]}"  # Set function name dynamically
    return test_func

# Add dynamically generated test functions to the module
for file in test_files:
    test_name = f"test_word_count_{os.path.splitext(file)[0]}"  # Dynamic function name
    globals()[test_name] = generate_test_function(file)
