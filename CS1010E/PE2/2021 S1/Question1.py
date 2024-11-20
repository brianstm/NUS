# PE 02

"""
Question 1: Parentheses
"""

"""
1.1 Iterative Parentheses
  Write the function to extract
  parentheses iteratively
"""


def extract_parentheses_I(stmt):
    result = ""
    for char in stmt:
        if char == '(' or char == ')':
            result += char
    return result


# Test cases (comment out or remove before copying to Coursemology)
print(extract_parentheses_I('(1+2)*(3+(4-5))'))
print(extract_parentheses_I('(1+2)*(3+(4-5)))'))
print(extract_parentheses_I('((1+2)*(3+(4-5))'))


"""
1.2 Recursive Parentheses
  Write the function to extract
  parentheses recursively
"""


def extract_parentheses_R(stmt):
    if len(stmt) == 0:
        return stmt
    else:
        if stmt[0] == '(' or stmt[0] == ')':
            return stmt[0] + extract_parentheses_R(stmt[1:])
        else:
            return extract_parentheses_R(stmt[1:])


# Test cases (comment out or remove before copying to Coursemology)
print(extract_parentheses_R('(1+2)*(3+(4-5))'))
print(extract_parentheses_R('(1+2)*(3+(4-5)))'))
print(extract_parentheses_R('((1+2)*(3+(4-5))'))


"""
1.3 Check Balanced
  Write the function to check if
  the parentheses are balanced
"""


def check_balanced_one(stmt):
    open, close = 0, 0
    for char in stmt:
        if char == '(':
            open += 1
        elif char == ')':
            close += 1
    return open == close


def check_balanced(stmt):
    balance = 0
    for char in stmt:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        # If at any point balance becomes negative 
        # (meaning there's a close parenthesis without
        # a matching open parenthesis)
        if balance < 0:
            return False
    # whether balance is 0, which would indicate that 
    # all parentheses are properly balanced
    return balance == 0


# Test cases (comment out or remove before copying to Coursemology)
print("CHECK BALANCE")
print(check_balanced_one('(1+2)*(3+(4-5))'))
print(check_balanced_one('(1+2)*(3+(4-5)))'))
print(check_balanced_one('((1+2)*(3+(4-5))'))
print(check_balanced_one(")("))

print("\nCHECK BALANCE CORRECT")
print(check_balanced('(1+2)*(3+(4-5))'))
print(check_balanced('(1+2)*(3+(4-5)))'))
print(check_balanced('((1+2)*(3+(4-5))'))
print(check_balanced(")("))
