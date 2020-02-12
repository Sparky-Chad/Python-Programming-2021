


def triangle(n):
    if n <= 1:
        print('*')
    else:
        triangle(n-1)
        print(n*"*")

def cascade(n):
    if n > 0:
        print(n * '*')
        cascade(n-1)
        print(n * '*')
    else:
        print(' ')

def countup(n):
    if n == 0:
        print(0)
    else:
        countup(n-1)
        print(n)

# Notice how the order of the print statement
# has a large effect as to the nature of the recursive
# code within the two examples here

def countdown(n):
    if n == 0:
        print(0)
    else:
        print(n)
        countdown(n-1)
