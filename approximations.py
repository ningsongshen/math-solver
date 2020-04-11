# Riemann sums
# taylor series
import math

# left riemann sums
def reciprocal(x):
    return 1 / x

def riemann(start, stop, f, interval):
    sum = 0
    if stop > start:
        i = start
        while i < stop:
            sum += f(i) * interval
            i += interval
        return sum
    elif stop < start:
        i = stop
        while i < start:
            sum += f(i) * interval
            i += interval
        return sum * -1
    else:
        return 0

def derivative(f, a):
    # doesn't work for second derivatives, therefore taylor doesn't work
    h = 0.000000001
    return (f(a+h) - f(a)) / h

def taylor(f, a, x, n):
    sum = 0
    d = f(a)
    i = 0
    while i < n:
        coefficient = d / math.factorial(i)
        term = (x-a) ** i
        sum += coefficient * term
        i += 1
        d = derivative(d, a)

    return sum

print(riemann(1, 1.5, reciprocal, 0.0001))

# doesn't work
print(taylor(reciprocal, 1, 2, 5))