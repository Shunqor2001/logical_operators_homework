def main(a):
    """
    Given a five-digit integer a,  check the following statement "All digits of the number are in ascending order".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    n1=a%10
    b=a//10
    n2=b%10
    d=b//10
    n3=d%10
    c=d//10
    n4=c%10
    f=c//10
    n5=f%10

    z = n1<n2<n3<n4<n5
    return z
print (main(12345))