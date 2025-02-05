# test_task6.py

import pytest
import task6
import os

# Define test files
test_files = ["task6_read_me.txt"]

# Expected word counts for each file (manually counted)
expected_word_counts = {
    "task6_read_me.txt": 91  # Ensure this matches the actual count from the file
}

# Metaprogramming: Dynamically generate test cases for each file
def generate_test_function(file_name):
    """Generates a test function dynamically for pytest."""
    def test_func():
        assert task6.count_words_in_file(file_name) == expected_word_counts[file_name]
    return test_func

# Add dynamically generated test functions to the module
for file in test_files:
    test_name = f"test_word_count_{os.path.splitext(file)[0]}"  # Dynamic function name
    globals()[test_name] = generate_test_function(file)
