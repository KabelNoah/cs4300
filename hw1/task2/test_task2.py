# test_task2.py

import task2

def test_get_integer():
    assert isinstance(task2.get_integer(), int)  # Ensure it returns an integer
    assert task2.get_integer() == 42  # Ensure value is correct

def test_get_float():
    assert isinstance(task2.get_float(), float)  # Ensure it returns a float
    assert task2.get_float() == 3.14  # Ensure value is correct

def test_get_string():
    assert isinstance(task2.get_string(), str)  # Ensure it returns a string
    assert task2.get_string() == "Hello, Python!"  # Ensure value is correct

def test_get_boolean():
    assert isinstance(task2.get_boolean(), bool)  # Ensure it returns a boolean
    assert task2.get_boolean() is True  # Ensure value is correct
