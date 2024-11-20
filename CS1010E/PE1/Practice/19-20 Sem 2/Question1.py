# PE 01

"""
Question 1: She Loves Me, She Loves Me Not
"""

"""
1.1 Rotating
  Write the function to rotate the bouquet
"""


def rotate(bouquet, step):
    bouquet = list(bouquet)
    for _ in range(step):
        tmp = bouquet[0]
        bouquet.pop(0)
        bouquet.append(tmp)

    return tuple(bouquet)


# Test data (do not modify)
bouquet = ("R", "P", "W", "W", "P", "R", "R", "R")
# Test cases (comment out or remove before copying to Coursemology)
print(rotate(bouquet, 2))
print(rotate(bouquet, 0))
print(rotate(bouquet, 8))
print(rotate(bouquet, 7))


"""
1.2 Iterative Flower
  Write the function to find the
  sequence of flower iteratively
"""


def flower_I(bouquet, k):
    bouquet = list(bouquet)
    result = ""

    for _ in range(len(bouquet)):
        bouquet = list(rotate(bouquet, k-1))
        selected_flower = bouquet.pop(0)
        result += selected_flower

    return result


# Test data (do not modify)
bouquet = ("R", "P", "W", "W", "P", "R", "R", "R")
# Test cases (comment out or remove before copying to Coursemology)
print(flower_I(bouquet, 3))
print(flower_I(bouquet, 8))
print(flower_I(bouquet, 7))


"""
1.3 Recursive Flower
  Write the function to find the
  sequence of flower recursively
"""


def flower_R(bouquet, k):
    bouquet = list(bouquet)

    if len(bouquet) == 1:
        return bouquet[0]
    else:
        bouquet = list(rotate(bouquet, k-1))
        selected_flower = bouquet.pop(0)
        remaining_flowers = flower_R(bouquet, k)
    return selected_flower + remaining_flowers


# Test data (do not modify)
bouquet = ("R", "P", "W", "W", "P", "R", "R", "R")
# Test cases (comment out or remove before copying to Coursemology)
print(flower_R(bouquet, 3))
print(flower_R(bouquet, 8))
print(flower_R(bouquet, 7))


"""
1.4 Pink Rose
  Write the function to find the
  smallest number to pink rose
"""


def pink_rose(bouquet):
    if len(bouquet) == 0 or "P" not in bouquet:
        return -1
    i = 0
    while True:
        seq = flower_I(bouquet, i)
        if seq[-1] == "P":
            return i
        i += 1


# Test data (do not modify)
bouquet = ("R", "P", "W", "W", "P", "R", "R", "R")
# Test cases (comment out or remove before copying to Coursemology)
print(pink_rose(bouquet))
