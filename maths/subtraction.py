"""
Calculate the subtraction of two numbers.

Source:
    https://en.wikipedia.org/wiki/Subtraction
"""


def subtraction(a: float, b: float) -> float:
    """
    >>> subtraction(10, 5)
    5
    >>> subtraction(5, 10)
    -5
    >>> subtraction(10.5, 5.5)
    5.0
    >>> subtraction(5.5, 10.5)
    -5.0
    >>> subtraction(10, 0)
    10
    >>> subtraction(0, 10)
    -10
    >>> subtraction(-5, 10)
    -15
    >>> subtraction(10, -5)
    15
    >>> subtraction(-5, -5)
    0
    >>> subtraction(0, 0)
    0
    """
    return a - b


if __name__ == "__main__":
    a = 5
    b = 6
    print(f"The subtraction of {a} - {b} is {subtraction(a, b)}")
