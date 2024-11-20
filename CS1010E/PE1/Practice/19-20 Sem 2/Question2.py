# PE 01

"""
Question 2: Bouquet
"""

"""
2.1 Making the Bouquet
  Write the function to check
  if making bouquet is possible
"""


def make_bouquet(shop, number):
    for i in range(len(shop)):
        for j in range(i, len(shop)):
            for k in range(j, len(shop)):
                if (shop[i][1] + shop[j][1] + shop[k][1] == number and
                        (shop[i][0] == 'P' or shop[j][0] == 'P' or shop[k][0] == 'P')):
                    return True
    return False


# Test data (do not modify)
flowers_r_us = [("R", 5, 3), ("R", 3, 2), ("W", 4, 3),
                ("W", 2, 2), ("P", 3, 4)]
# Test cases (comment out or remove before copying to Coursemology)
print(make_bouquet(flowers_r_us, 10))
print(make_bouquet(flowers_r_us, 14))
print(make_bouquet(flowers_r_us, 2))


"""
2.2 Minimum Cost
  Write the function to find
  the minimum cost if possible
"""


def minimum_cost(shop, number):
    min_cost = -1
    for i in range(len(shop)):
        for j in range(i, len(shop)):
            for k in range(j, len(shop)):
                if (shop[i][1] + shop[j][1] + shop[k][1] == number and
                        (shop[i][0] == 'P' or shop[j][0] == 'P' or shop[k][0] == 'P')):
                    cost = shop[i][2] + shop[j][2] + shop[k][2]
                    if min_cost == -1 or cost < min_cost:
                        min_cost = cost
    return min_cost


# Test data (do not modify)
flowers_r_us = [("R", 5, 3), ("R", 3, 2), ("W", 4, 3),
                ("W", 2, 2), ("P", 3, 4)]
# Test cases (comment out or remove before copying to Coursemology)
print(minimum_cost(flowers_r_us, 10))
print(minimum_cost(flowers_r_us, 14))
print(minimum_cost(flowers_r_us, 2))
