def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    num1=a//10
    num2=a%10
    n =num1+num2
    return n%2!=0
print(main(55))