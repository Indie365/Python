"""
Consecutive prime sum

Problem 50

The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to
a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime,
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of
the most consecutive primes?
"""

"""
Solution:

First of all, we need to generate all prime numbers
from 2 to the closest prime number with 1000000.
Then, use sliding window to get the answer.
"""

from math import floor, sqrt


def is_prime(number: int) -> bool:
    """
    function to check whether a number is a prime or not.
    >>> is_prime(2)
    True
    >>> is_prime(6)
    False
    >>> is_prime(1)
    False
    """

    if number < 2:
        return False

    for n in range(2, floor(sqrt(number)) + 1):
        if number % n == 0:
            return False

    return True


def solution():
    """
    Return the problem solution.
    >>> solution()
    997651
    """

    prime_list = [2] + [x for x in range(3, 10 ** 6, 2) if is_prime(x)]

    cumulative_sum = []
    tmp = 0
    for x in prime_list:
        tmp += x
        if tmp < 10 ** 6:
            cumulative_sum.append(tmp)
        else:
            break

    upper_limit_idx = 0
    for i in range(len(prime_list)):
        if prime_list[i] < 10 ** 6:
            upper_limit_idx = i
        else:
            break

    max_count = -1
    answer = 0
    for number in reversed(cumulative_sum):
        count_prime = cumulative_sum.index(number) + 1

        if not is_prime(number):
            tmp = number

            for i in range(upper_limit_idx):
                count_prime -= 1
                tmp -= prime_list[i]

                if is_prime(tmp) or tmp < 0:
                    break

        if max_count < count_prime:
            max_count = count_prime
            answer = tmp

    return answer


if __name__ == "__main__":
    print(solution())
