# PE 01

"""
Question 1: Happy Numbers
"""

"""
1.1 Iterative SDS
  Write the function to compute SDS iteratively
"""


def sum_digit_square_I(n):
    sum = 0
    while n > 0:
        digit = n % 10
        sum += digit**2
        n //= 10
    return sum


# Test cases (comment out or remove before copying to Coursemology)
print(sum_digit_square_I(123456))
print(sum_digit_square_I(987654321))
print(sum_digit_square_I(999988887777666655554444333322221111))


"""
1.2 Recursive SDS
  Write the function to compute SDS recursively
"""


def sum_digit_square_R(n):
    if n == 0:
        return 0
    else:
        return (n % 10)**2 + sum_digit_square_R(n // 10)


# Test cases (comment out or remove before copying to Coursemology)
print(sum_digit_square_R(123456))
print(sum_digit_square_R(987654321))
print(sum_digit_square_R(999988887777666655554444333322221111))


"""
1.3 Single Happy Number
  Write the function to check
  if a number n is happy
"""


def is_happy_number(n):
    prev = []
    while n != 1:
        if n in prev:
            return False
        else:
            prev.append(n)
            n = sum_digit_square_I(n)
    return True


# Test cases (comment out or remove before copying to Coursemology)
print(is_happy_number(83))
print(is_happy_number(849))
print(is_happy_number(10888))
print(is_happy_number(100093))


"""
1.4 All Happy Number
  Write the function to find
  all happy numbers
"""


def all_happy_number(n, m):
    result = []
    for i in range(n, m+1):
        if is_happy_number(i):
            result.append(i)
    return result


# Test cases (comment out or remove before copying to Coursemology)
print(all_happy_number(1, 70))
