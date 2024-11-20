# PE 02

"""
Question 3: Fun with Digits
"""

"""
3.1 Equal To
  Write the function to find
  correct equations
"""


def equal_to(lhs, rhs, ops):
    """
    1) Get all possible equations (insert ops at different index of lhs)
    2) Eval the expression and check if equal to rhs
    3) For valid expressions, add to set expression + '=rhs'
    """
    ans = set()
    # Convert to list so we can iterate over empty string for convenience
    ops = list(ops) + ['']
    eqns = [lhs[0]]

    # Iteratively get all possible combinations
    for digit in lhs[1:]:
        next_eqns = []
        for eqn in eqns:
            for op in ops:
                next_eqns.append(eqn + op + digit)
        eqns = next_eqns

    # Add to set the valid equations
    for eqn in eqns:
        if eval(eqn) == rhs:
            ans.add(eqn + f'={rhs}')

    return ans


# Test cases (comment out or remove before copying to Coursemology)
print(equal_to('199', 100, '+'))
# print(equal_to('123456789', 100, '+-'))
# print(equal_to('111111', 100, '+-*%'))
