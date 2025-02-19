# task7.py

import numpy as np

def generate_random_array(size):
    """Generates a NumPy array of random numbers between 0 and 1."""
    return np.random.rand(size)

def compute_mean(array):
    """Computes the mean of a NumPy array."""
    return np.mean(array)

if __name__ == "__main__":
    sample_array = generate_random_array(10)
    mean = compute_mean(sample_array)
    print(f"Generated Array: {sample_array}")
    print(f"Mean: {mean:.4f}")
