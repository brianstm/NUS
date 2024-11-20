# PE 02

"""
Question 1: Calculus
"""


def compute(poly, x):  # You don't have to understand this, it works
    return sum(poly[i]*x**i for i in range(len(poly)))


"""
1.1 Iterative Derivative
  Write the function to compute
  the derivative iteratively
"""


def derivative_I(poly):
    result = []
    for i in range(1, len(poly)):
        result.append(i*poly[i])
    return result

def derivative_I_2(poly):
    return [poly[1]] + [i * poly[i] for i in range(2, len(poly))]


# Test cases (comment out or remove before copying to Coursemology)
# print(derivative_I([3, -9, 1, 2]))
# print(derivative_I([-9, 2, 6]))
# print(derivative_I_2([3, -9, 1, 2]))
# print(derivative_I_2([-9, 2, 6]))

"""
1.2 Recursive Derivative
  Write the function to compute
  the derivative recursively
"""


def derivative_R(poly):
    if len(poly) == 1:
        return []
    else:
        return derivative_R(poly[:-1]) + [(len(poly) - 1) * poly[-1]]


# Test cases (comment out or remove before copying to Coursemology)
# print(derivative_R([3, -9, 1, 2]))
# print(derivative_R([-9, 2, 6]))


"""
1.3 Newton's Method
  Write the function to find
  the root of a polynomial
  using Newton's method
"""


def newton(poly, x0):
    xn = x0
    while True:
        xn = xn - compute(poly, xn) / compute(derivative_I(poly), xn)
        if abs(compute(poly, xn)) < 0.00001:
            return xn


# Test cases (comment out or remove before copying to Coursemology)
print(newton([3, -9, 1, 2], 2))
print(newton([3, -9, 1, 2], 0))
print(newton([3, -9, 1, 2], -2))
