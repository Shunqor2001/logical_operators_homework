def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits of the number are the same".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    tens_digit = a // 10
    units_digit = a % 10
    
    return tens_digit == units_digit

print(main(22))