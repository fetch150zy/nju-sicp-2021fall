def both_odd(a, b):
    """Returns True if both a and b are odd numbers.

    >>> both_odd(-1, 1)
    True
    >>> both_odd(2, 1)
    False
    """
    return a % 2 == 1 and b % 2 == 1 # You can replace this line!


def factorial(n):
    """Return the factorial of a positive integer n.

    >>> factorial(3)
    6
    >>> factorial(5)
    120
    """
    cnt = 1
    for i in range(1, n + 1):
        cnt *= i
    return cnt

def is_triangle(a, b, c):
    """Given three integers (may be nonpositive), judge whether the three
    integers can form the three sides of a triangle.

    >>> is_triangle(2, 1, 3)
    False
    >>> is_triangle(5, -3, 4)
    False
    >>> is_triangle(2, 2, 2)
    True
    """
    return a+b>c and a+c>b and b+c>a


def number_of_six(n):
    """Return the number of 6 in each digit of a positive integer n.

    >>> number_of_six(666)
    3
    >>> number_of_six(123456)
    1
    """
    # return str(n).count('6')
    cnt = 0
    while n != 0:
        if n % 10 == 6:
            cnt += 1
        n //= 10
    return cnt


def max_digit(x):
    """Return the max digit of x.

    >>> max_digit(10)
    1
    >>> max_digit(4224)
    4
    >>> max_digit(1234567890)
    9
    >>> # make sure that you are using return rather than print
    >>> a = max_digit(123)
    >>> a
    3
    """
    res = 0
    while x != 0:
        t = x % 10
        if res < t:
            res = t
        if res == 9:
            return res
        x //= 10
    return res
