"""
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number,
134217728=89, is a ninth power.
How many n-digit positive integers exist which are also an nth power?
"""

"""
The maximum base can be 9 because all n-digit numbers < 10^n.
Now 9**23 has 22 digits so the maximum power can be 22.
Using these conclusions, we will calculate the result.
"""


def compute_nums(max_base: int = 10, max_power: int = 22) -> int:
    """
    Returns the count of all n-digit numbers which are nth power
    >>> compute_nums(10, 22)

    49
    """
    bases = list(range(1, max_base))
    powers = list(range(1, max_power))
    count = 0
    for base in bases:
        for power in powers:
            if len(str((base ** power))) == power:
                count += 1
    return count


if __name__ == "__main__":
    print(f"{compute_nums(10, 22) = }")
