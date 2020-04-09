# Test function e^x - 2
# Newton's method
# Fixed point iteration method

import math

def testf(x):
    return math.exp(x) - 2

def dtestf(x):
    return math.exp(x)

def newton(f, df, x0, iterations):
    xn = x0
    for i in range(iterations):
        xn = xn - (f(xn) / df(xn))
    return xn

def test2f(x):
    return math.sqrt(x)

def fixed_point(f, x0, iterations):
    xn = x0
    for i in range(iterations):
        xn = f(xn)
    return xn

print(newton(testf, dtestf, 5, 2000))
print(fixed_point(test2f, 2, 100))