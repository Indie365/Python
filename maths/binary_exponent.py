def bin_exp(num: int, expo: int) -> int:
    """
    Calculate the exponent of 'num' over 'expo' and return a positive number.
    This function does binary exponential hence O(log N) time complexity.
    So, It is faster than normal exponential function for huge numbers.
    >>> bin_exp(2, 5)
    32
    >>> bin_exp(1,0)
    1
    >>> bin_exp(-2, 0)
    1
    >>> bin_exp(-2, -2)
    0
    >>> bin_expo(1.5, 2.5)
    2
    >>> bin_expo('a', 'b')
    TypeError: can't multiply sequence by non-int of type 'str'
    >>> bin_expo(5, None)
    TypeError: can't multiply sequence by non-int of type 'str'
  
    """
    result = 1
    while expo:
        div, mod = divmod(expo, 2)
        if mod:
            result *= num
            expo -= 1
        else:
            num *= num
            expo = div
    return result


# call the testmod function
if __name__ == "__main__":
    from doctest import testmod

    testmod()
