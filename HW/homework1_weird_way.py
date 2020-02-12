
from math import ceil


def egypt(n,d):
    """egypt(n, d) will return the sum of unit factors to n/d
    1/x + 1/y = n/d

    >>> egypt(3,4)
    '1/2 + 1/4 = 3/4'
    >>> egypt(11,12)
    '1/2 + 1/3 + 1/12 = 11/12'
    >>> egypt(103,104)
    '1/2 + 1/3 + 1/7 + 1/71 + 1/9122 + 1/141449381 = 103/104'
    >>> egypt(123,124)
    '1/2 + 1/3 + 1/7 + 1/64 + 1/8333 + 1/347186112 = 123/124'
    >>> egypt(2,1)
    'Invalid Fraction'
    """
    "*** YOUR CODE HERE ***"

    output = ""
    fractions = f"{n}/{d}"

    # Perform validity checks
    if n == 0:
        return f'0 = {n}/{d}'
    if n > d or d == 0:
        return 'Invalid Fraction'

    while True:

        # Check if the numerator devides the denominator evenly
        # has a small error due to small problems with rounding

        #if n / d < 1/4000000000:
        if n <= 0:
            #Remove the excess '+' and then add on the original fraction
            output =  output[0: len(output)- 2] + f'= {fractions}'
            
            return output
        
        else:
            temp = ceil(d / n)

            output = output + f'1/{temp} + '

            """
            Now this will take the fraction and subtract the unit from it
            n * temp     d * 1      new n
            -   ---- - --------- = -------
            d * temp    d * temp    new d
            
            this ensures there are no dirty fractions ever
            """

            n = n * temp - d
            d = d * temp
ceil


import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)
