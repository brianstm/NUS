# PE 02

"""
Question 1: Super Fibonacci Sequence
"""

"""
1.1 Recursive SFS
  Write the function to compute
  the first n SFS recursively
"""


def super_fib_R(term2, n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, term2]
    else:
        result = super_fib_R(term2, n-1)
        result.append(sum(result))
        return result


# Test cases (comment out or remove before copying to Coursemology)
print(super_fib_R(10, 10))
print(super_fib_R(20, 7))
print(super_fib_R(11, 994)[-1] % 10000)
print(super_fib_R(11, 994)[-2] % 10000)


"""
1.2 Iterative SFS
  Write the function to compute
  the SFS smaller than upper iteratively
"""


def super_fib_I(term2, upper):
    result = [1, term2]
    total = sum(result)
    while total <= upper:
        result.append(total)
        total *= 2
    return result


# Test cases (comment out or remove before copying to Coursemology)
print(super_fib_I(4, 100))
print(super_fib_I(4, 160))
print(len(super_fib_I(20, 10**4321)))
print(super_fib_I(20, 10**4321)[-1] % (10**10))


"""
1.3 Smallest Second
  Write the function to compute
  the smallest second term
"""


# def smallest_second(n):
#     term2 = 2
#     while True:
#         sequence = super_fib_I(term2, n)
#         if n in sequence:
#             return term2
#         term2 += 1

def smallest_second(n):
    """
    n is either term2+1 or a multiple of (term2 + 1)
    Edge case: n = 2. Then we don't divide it anymore! 
    Since smallest term2 will be 1 (1+term2 = 2)
    """
    ans = n
    while not n % 2 and n > 2:
        n //= 2
        ans = min(ans, n)

    return ans - 1


# Test cases (comment out or remove before copying to Coursemology)
print(smallest_second(2016))
print(smallest_second(9876))
print(smallest_second(23592960))
print(smallest_second(2651336998912))
