"""
Project Euler Problem 100: https://projecteuler.net/problem=100

Arranged probability
Problem 100
If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs,
and two discs were taken at random, it can be seen that the probability of taking two blue discs,
P(BB) = (15/21)×(14/20) = 1/2.
The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random,
is a box containing eighty-five blue discs and thirty-five red discs.
By finding the first arrangement to contain over 10 ^ 12= 1,000,000,000,000 discs in total,
determine the number of blue discs that the box would contain.
"""

def solution() -> int:
    """
    For this solution we have the generalized equation
     X        (X-1) =    1
    ____   *  _____     ___
     N        N - 1      2

     we can turn it into

     2x^2 - 2x - N^2 + N = 0

     Thats a quadratic diophantine equation

     we can use this site to generate a recursive solution for our equation https://www.alpertron.com.ar/QUAD.HTM
     the input should be
      2
      0
     -1
     -2
      1
      0
      it return the functions to retreive X and N
      Xn+1 = 3 X + 2 N - 2
      Nn+1 = 4 X + 3 N - 3
      so lets code that.
    >>> solution()
    756872327473
    """
    # the number of the first arrange of blue disks that taken 2 in a row return 50% of prob to happen
    blueDisks = 85
    # the number of the first total disks to this probability happen
    totalDisks = 120
    # the maximum lenght of totalDisks to find the blue and Total that has 0.5 probability to be picked in a row
    total_lenght = 1 * (10 ** 12)

    while totalDisks <= total_lenght:
        """ 
        x = blueDisks
        n = totalDisks
        Xn+1 = 3 X + 2 N - 2
        Nn+1 =  4 X + 3 N - 3
        apply this functions to get the correct values
        """
        """
        We have to set this variables separated by commas so in totalDisks attribution the value in blueDisks
        will be the value setted before the current while iteration
        """
        blueDisks, totalDisks = (3 * blueDisks) + (2 * totalDisks) - 2, (4 * blueDisks) + (3 * totalDisks) - 3

    return blueDisks
if __name__ == "__main__":
    print(f'blueDiskQuantity: {solution()}')
