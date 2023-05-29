def main(x):
    """
    Given a two digit integer x, return true if x is palindrome integer.
    An integer is a palindrome, when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    tens_digit = x // 10
    units_digit = x % 10
    return tens_digit == units_digit
print(main())