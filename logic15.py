def main(a):
    """
    Given a three-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    num1 = a // 100
    num2 = (a // 10) % 10
    num3 = a % 10
    
    digit_sum = num1 + num2 + num3
    
    return digit_sum % 2 != 0
print(main(123))