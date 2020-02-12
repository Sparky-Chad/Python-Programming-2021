##Lab04 Required Questions ##

#########
# Lists #
#########

# RQ1
def cascade(lst):
    """Returns the cascade of the given list.

    >>> cascade([1, 2, 3, 4])
    [1, 2, 3, 4, 4, 3, 2, 1]
    """
    "*** YOUR CODE HERE ***"
    arg = []
    arg.extend(lst)
    arg.reverse()
    lst.extend(arg)
    return lst

# RQ2
def maptwice(fn, seq):
    """Applies fn twice onto each element in seq and returns the resulting list.

    >>> maptwice(lambda x: x*x, [1, 2, 3])
    [1, 16, 81]
    """
    "*** YOUR CODE HERE ***"
    return list(map(fn,list(map(fn, seq))))

#RQ3
def filterout(pred, seq):
    """Keeps elements in seq only if they do not satisfy pred.

    >>> filterout(lambda x: x % 2 == 0, [1, 2, 3, 4])
    [1, 3]
    """
    "*** YOUR CODE HERE ***"
    arg = tuple(filter(pred, seq))
    # Defines a quick helper function to return what isn't in that
    def helper(x):
        for i in arg:
            if x == i:
                return False
        return True
    return list(filter(helper, seq))

#RQ4
def comp(n, pred):
    """ Uses a one line list comprehension to return list of the first n integers (0...n-1) which satisfy the predicate pred.
    >>> comp(7, lambda x: x%2 ==0)
    [0, 2, 4, 6]
    """
    "*** YOUR CODE HERE ***"
    # Returns a list initialized with an inline for loop and the filtered
    return list(filter(pred, [i for i in range(0,n)]))
    
#RQ5
def flatten(lst):
    """ Takes a nested list and "flattens" it.
    
    >>> flatten([1, 2, 3]) 
    [1, 2, 3]
    >>> x = [1, [2, 3], 4]      
    >>> flatten(x)
    [1, 2, 3, 4]
    >>> x = [[1, [1, 1]], 1, [1, 1]] 
    >>> flatten(x)
    [1, 1, 1, 1, 1, 1]
    >>> lst = [1, [[2], 3], 4, [5, 6]]
    >>> flatten(lst)
    [1, 2, 3, 4, 5, 6]
    """
    "*** YOUR CODE HERE ***"

    # For this function, just iterate through it, creating a new copy list
    # Each time a list is found, take those objects and put them in
    out = []
    for i in lst:
        if type(i) == list:
            # Returns a flattened list of that list
            out.extend(flatten(i))
        else:
            out.append(i)
    
    return out             


import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)