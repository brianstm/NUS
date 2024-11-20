# PE 01

"""
Question 2: Unique Sequence
"""

"""
2.1 Simple Unique Sequence
  Write the function to check
  if the sequence is unique
"""


def is_unique(seq):
    for i in range(len(seq)):
        for j in range(i+1, len(seq)):
            if seq[i] == seq[j]:
                return False
    return True


# Test cases (comment out or remove before copying to Coursemology)
print(is_unique('minions'))
print(is_unique('abcdefghijklmnopqrstuvwxyz'))
print(is_unique([1, 2, 3, 4, 5, 6, 7, 8]))
print(is_unique(['a', 'b', 3, True, 999, 'a']))
print(is_unique((1, 2, 999, 4, 0, 6, (1, 2), 999)))
print(is_unique(['aaa', 'bbb', (1, 1), 1]))


"""
2.2 Complex Unique Sequence
  You get this automatically
  if you don't use len and range
  on top of other restrictions
"""


def is_unique_2(seq):
    for index, i in enumerate(seq):
        # enumerate('minions') gives
        # (0, 'm')
        # (1, 'i')
        # (2, 'n')
        # (3, 'i')
        # (4, 'o')
        # (5, 'n')
        # (6, 's')
        new_seq = seq[index+1:]
        for j in new_seq:
            # index:  0 | 1st:  m | 2nd:  i
            # index:  0 | 1st:  m | 2nd:  n
            # index:  0 | 1st:  m | 2nd:  i
            # index:  0 | 1st:  m | 2nd:  o
            # index:  0 | 1st:  m | 2nd:  n
            # index:  0 | 1st:  m | 2nd:  s
            # index:  1 | 1st:  i | 2nd:  n
            # index:  1 | 1st:  i | 2nd:  i
            if i == j:
                return False
    return True


print("")
print(is_unique_2('minions'))
# print(is_unique_2('abcdefghijklmnopqrstuvwxyz'))
# print(is_unique_2([1, 2, 3, 4, 5, 6, 7, 8]))
# print(is_unique_2(['a', 'b', 3, True, 999, 'a']))
# print(is_unique_2((1, 2, 999, 4, 0, 6, (1, 2), 999)))
# print(is_unique_2(['aaa', 'bbb', (1, 1), 1]))
