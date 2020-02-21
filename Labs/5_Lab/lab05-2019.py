## Lab 5: Required Questions - Dictionaries Questions ##

# RQ1
def merge(dict1, dict2):
    """Merges two Dictionaries. Returns a new dictionary that combines both. You may assume all keys are unique.

    >>> new =  merge({1: 'one', 3:'three', 5:'five'}, {2: 'two', 4: 'four'})
    >>> new == {1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five'}
    True
    """
    "*** YOUR CODE HERE ***"
    for i in dict2:
        dict1[i] = dict2[i]
    return dict1


# RQ2
def counter(message):
    """ Returns a dictionary of each word in message mapped
    to the number of times it appears in the input string.
    >>> x = counter('to be or not to be')
    >>> x['to']
    2
    >>> x['be']
    2
    >>> x['not']
    1
    >>> y = counter('run forrest run')
    >>> y['run']
    2
    >>> y['forrest']
    1
    """
    "*** YOUR CODE HERE ***"
    out = {}
    for i in message.split():
        if i not in out:
            out[i] = 1
        else:
            out[i] += 1
    return out

# RQ3
def replace_all(d, x, y):
    """
    >>> d = {'foo': 2, 'bar': 3, 'garply': 3, 'xyzzy': 99}
    >>> replace_all(d, 3, 'poof')
    >>> d == {'foo': 2, 'bar': 'poof', 'garply': 'poof', 'xyzzy': 99}
    True
    """
    "*** YOUR CODE HERE ***"
    # Was looking into one line for loops and stuff, so its a mess    
    r = {i: d[i] if d[i] != x else y for i in d }
    return r
# RQ4
def sumdicts(lst):
    """ 
    Takes a list of dictionaries and returns a single dictionary which contains all the keys value pairs. And 
    if the same key appears in more than one dictionary, then the sum of values in list of dictionaries is returned 
    as the value for that key
    >>> d = sumdicts ([{'a': 5, 'b': 10, 'c': 90, 'd': 19}, {'a': 45, 'b': 78}, {'a': 90, 'c': 10}] )
    >>> d == {'b': 88, 'c': 100, 'a': 140, 'd': 19}
    True
    """
    "*** YOUR CODE HERE ***"
    sumout = {}
    # Run through list of dicts
    for i in lst:
       # Run through each list
        for j in i:
            # Add to sum
            if j not in sumout:
                sumout[j] = i[j]
            else:
                sumout[j] += i[j]
    return sumout
#RQ5
def middle_tweet(word, table):
    """ Calls the function random_tweet() 5 times (see Interactive Worksheet) and 
    returns the one string that is of length right in middle of the 5.
    Returns a string that is a random sentence of average length starting with word, and choosing successors from table.
    """
    "*** YOUR CODE HERE ***"
    def construct_tweet(word, table):
        """Returns a string that is a random sentence starting with word, and choosing successors from table.
        """
        import random
        result = ' '
        while word not in ['.', '!', '?']:
            result += word + ' '
            word = random.choice(table[word])
        return result + word

    from math import ceil
    current_list = []
    # Call construct tweet 5 times into a list
    # So that it then has 5 sentances of the length of 
    for i in range(0,5):
        current_list.append(construct_tweet(word, table))
    # Sort by length
    for i in range(0, len(current_list)):
        for j in range(0, len(current_list)):
            # Now begin to sort the lests by length
            if len(current_list[i]) > len(current_list[j]):
                temp = current_list[i]
                current_list[i] = current_list[j]
                current_list[j] = temp
    # The return the central most one, this serves as the median(which is an average type) of the 
    # list lengths
    return current_list[ceil(len(current_list)/2)]
    


    

import doctest
if __name__ == "__main__":
  doctest.testmod(verbose=True)

# Inputing some of the code from the lab
def shakespeare_tokens(path='shakespeare.txt', url='http://composingprograms.com/shakespeare.txt'):
    #"""Return the words of Shakespeare's plays as a list."""
    import os
    from urllib.request import urlopen
    if os.path.exists(path):
        return open('shakespeare.txt', encoding='ascii').read().split()
    else:
        shakespeare = urlopen(url)
        return shakespeare.read().decode(encoding='ascii').split()
def build_successors_table(tokens):
    table = {}
    prev = '.'
    for word in tokens:
        if prev not in table:
            table[prev] = []
        table[prev] += [word]
        prev = word
    return table