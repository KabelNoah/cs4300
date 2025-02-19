# test_task7.py

import pytest
import task7
import numpy as np

def test_generate_random_array():
    array = task7.generate_random_array(5)
    assert isinstance(array, np.ndarray)  # Ensure it returns a NumPy array
    assert len(array) == 5  # Ensure the array has the correct size

def test_compute_mean():
    test_array = np.array([1, 2, 3, 4, 5])
    mean = task7.compute_mean(test_array)

    assert mean == pytest.approx(3.0, rel=1e-3)  # Mean should be 3.0
