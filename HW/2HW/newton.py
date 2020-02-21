# HW 2 Newton
# By Chad Lape

from math import sin, cos
# Constant for 15 digits of accuracy
ACCURACY = float(1.0E-15)
PI = lambda x: sin(x) + x
NPI = lambda x: sin(x)
dPI = lambda x: cos(x)
p1 = 3.0

# Defined Exception class for if divergent
class DivergentIterationError(Exception):
    # Just as an exception
    pass

# Fixed point iteration
def fixed_point_iteration(f, x=1.0, step=0):
    # Helper for iteration
    def approx_fixed_point(f, x):
        # This can return true only if f(x) and x is very close in distance
        # In essence that the difference between last and new is < 1E-15
        return abs(f(x) - x) < ACCURACY
    
    # This works by calling the helper to decide whether the current point meets specifications
    # if this is not the case it will call itself again to repeat and continue to have another point
    # of accuracy, this can continue for a long time and 
    if approx_fixed_point(f, x):
        return x, step
    elif step > 1000:
        raise DivergentIterationError(step)
        # Just an exception to prevent an infinite loop from starting and causing a program
        # crash due to running to long
    return fixed_point_iteration(f, x=f(x), step=step+1)

def newton_find_zero(f, df, x, step=0):
    # Update Function
    update = lambda f, df: x - (f(x) / df(x))
    # So this will compute a location for x to be 0 along the tangent line and then this will in time bring x
    # ever closer to an actual theoretical 0
    # Function for if x is at a zero
    zero = lambda x, f: abs(f(x)) < ACCURACY
    # Thus we can compute this to where x will be it
    def improve_x(x):
        x = update(f, df)
        return x
    
    while not zero(x, f):
        x = improve_x(x)
        step = step + 1
    return x, step
    # Performs iteratively using higher order functions



