


# function to find the largest unit factor
# 
# Will return only the largest denomenator of the unit factor 
def find_largest_unit(numer, denomer, unit=1):
    # when to trigger the fib_find
    bad_unit = 10000 + unit

    # fib_find will use a fibbonachi sequence to find the closest number
    # to what this might be. This will help to decrease the number of checks which
    # occurs to decrease run time. 
    def fib_find(current=1, past=0):
        if (numer * (unit+current) - denomer) > 0:
            return past
        else:
            return fib_find(current=current+past, past=current)
    # END HELPER

    # loop until the if condition is met
    while True:

        # This way of testing is useful as due to this way it will never have weird
        # fractions.
        #  numer * unit              denomer
        # --------------    -   ---------------
        # denomer * unit         denomer * unit
        #
        # hopefully

        # Uses an algorithm similar to the greedy algorithm to find the greatest
        # unit fraction which fits within the fraction
        if (numer * unit - denomer) >= 0:
            #only return if it can find one where numer is greater than 0
            return unit 
        unit += 1
        if unit == bad_unit:
            unit += fib_find()
            bad_unit = unit + 1000

def egypt(n,d):
    # Found answers for testing using the following calculator
    # http://www.calcul.com/show/calculator/egyptian-fraction?n=103&d=104 
    """egypt(n, d) will return the sum of unit factors to n/d
    1/x + 1/y = n/d

    >>> egypt(3,4)
    '1/2 + 1/4 = 3/4'
    >>> egypt(11,12)
    '1/2 + 1/3 + 1/12 = 11/12'
    >>> egypt(103,104)
    '1/2 + 1/3 + 1/7 + 1/71 + 1/9122 + 1/141449381 + 1/100039636784966424 = 103/104'
    >>> egypt(123,124)
    '1/2 + 1/3 + 1/7 + 1/64 + 1/8333 + 1/347186112 = 123/124'
    >>> egypt(1000,1001)
    '1/2 + 1/3 + 1/7 + 1/44 + 1/12012 = 1000/1001'
    """
    # Store original fraction
    orig = f'{n}/{d}'
    # Past unit factor denominator
    u = 1
    # current unit factors
    unit_denoms = []
    # Will run until n is 0
    while n != 0:
        # find largest unit factor 
        u = find_largest_unit(n, d, u)
        # Update n and d
        n = n * u - d
        d = d * u
        # Add unit fraction
        unit_denoms.append(u)
    
    # Return the unit fractions in string format
    out = ""
    for i in unit_denoms:
        out += f'1/{i} + '
    out = out[0:len(out)-2]
    out += f'= {orig}'
    return out

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)

