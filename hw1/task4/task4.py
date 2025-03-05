# task4.py

def calculate_discount(price, discount):
    """
    Calculates the final price after applying a discount percentage.
    Accepts any numeric type for price and discount.
    
    :param price: The original price (int or float).
    :param discount: The discount percentage (int or float).
    :return: The final price after discount.
    """
    if not isinstance(price, (int, float)) or not isinstance(discount, (int, float)):
        raise TypeError("Both price and discount should be numbers")

    if discount < 0 or discount > 100:
        raise ValueError("Discount must be between 0 and 100")

    return price * (1 - discount / 100)
