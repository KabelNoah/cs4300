# task3.py

def check_number(n):
    """Checks if a number is positive, negative, or zero."""
    if n > 0:
        return "Positive"
    elif n < 0:
        return "Negative"
    else:
        return "Zero"

def first_n_primes(n=10):
    """Returns a list of the first `n` prime numbers."""
    primes = []
    num = 2
    while len(primes) < n:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes

def sum_to_100():
    """Finds the sum of all numbers from 1 to 100 using a while loop."""
    total = 0
    num = 1
    while num <= 100:
        total += num
        num += 1
    return total
