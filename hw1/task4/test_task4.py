# test_task4.py

import pytest
import task4

def test_calculate_discount():
    # Test with integers
    assert task4.calculate_discount(100, 10) == 90  # 10% off 100 = 90
    assert task4.calculate_discount(200, 25) == 150  # 25% off 200 = 150

    # Test with floats
    assert task4.calculate_discount(99.99, 5) == pytest.approx(94.99, rel=1e-2)  # 5% off 99.99
    assert task4.calculate_discount(50.5, 20.5) == pytest.approx(40.17, rel=1e-2)  # 20.5% off 50.5

    # Test zero discount
    assert task4.calculate_discount(100, 0) == 100  # No discount, same price

    # Test 100% discount
    assert task4.calculate_discount(100, 100) == 0  # Full discount, price is 0

    # Test invalid inputs (should raise errors)
    with pytest.raises(TypeError):
        task4.calculate_discount("100", 10)  # Price as string

    with pytest.raises(TypeError):
        task4.calculate_discount(100, "10")  # Discount as string

    with pytest.raises(ValueError):
        task4.calculate_discount(100, -5)  # Negative discount

    with pytest.raises(ValueError):
        task4.calculate_discount(100, 105)  # Discount over 100%
