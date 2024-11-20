# PE 02

"""
Question 2: Cousins
"""

"""
2.1 Are You My Cousins
  Write the function to check if
  the two people are cousins
"""


# def is_cousin(name1, name2, tree):
#     if name1 not in tree or name2 not in tree:
#         return False

#     new_name1, new_name2 = name1, name2
#     for _ in range(2):
#         new_name1 = tree[new_name1]
#         new_name2 = tree[new_name2]

#     return new_name1 == new_name2


def is_cousin(name1, name2, tree):
    if name1 not in tree or name2 not in tree:
        return False
    if name1 == name2:
        return False
    if tree[name1] == tree[name2]:
        return False
    new_name1, new_name2 = tree[name1], tree[name2]
    if not new_name1 in tree or not new_name2 in tree:
        return False
    return tree[new_name1] == tree[new_name2]


# Test data (do not modify)
parent = {
    'Amy': 'Ben', 'Tom': 'Ben', 'Frank': 'Amy',
    'May': 'Tom', 'Ben': 'Howard', 'Howard': 'George',
    'Jane': 'May', 'Joe': 'Frank',  # second cousin
    'Liz': 'Jane', 'Alf': 'Joe'      # third cousin
}
# Test cases (comment out or remove before copying to Coursemology)
print(is_cousin('Frank', 'May', parent))
print(is_cousin('Jane', 'Joe', parent))
print(is_cousin('Liz', 'Alf', parent))


"""
2.2 N-th Cousin
  Write the function to find
  the value of n such that
  the two people are n-th cousin
"""


# def nth_cousin(name1, name2, tree):
#     new_name1, new_name2, i = name1, name2, 0
#     while True:
#         if new_name1 in tree and new_name2 in tree:
#             new_name1 = tree[new_name1]
#             new_name2 = tree[new_name2]

#             if new_name1 == new_name2:
#                 return i

#             i += 1
#         else:
#             return -1

def nth_cousin(name1, name2, tree):
    if name1 not in tree or name2 not in tree:
        return -1
    if name1 == name2:
        return -1
    new_name1, new_name2, i = name1, name2, 0
    while True:
        if new_name1 in tree and new_name2 in tree:
            new_name1 = tree[new_name1]
            new_name2 = tree[new_name2]

            if new_name1 == new_name2:
                return i

            i += 1
        else:
            return -1


# Test cases (comment out or remove before copying to Coursemology)
print(nth_cousin('Frank', 'May', parent))
print(nth_cousin('Jane', 'Joe', parent))
print(nth_cousin('Liz', 'Alf', parent))
print(nth_cousin('Frank', 'Alf', parent))
