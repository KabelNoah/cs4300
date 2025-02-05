# test_task3.py

import task3

def test_check_number():
    assert task3.check_number(10) == "Positive"
    assert task3.check_number(-5) == "Negative"
    assert task3.check_number(0) == "Zero"

def test_first_n_primes():
    assert task3.first_n_primes(10) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert task3.first_n_primes(5) == [2, 3, 5, 7, 11]

def test_sum_to_100():
    assert task3.sum_to_100() == 5050  # The sum of numbers from 1 to 100
