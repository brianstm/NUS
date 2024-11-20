# PE 02

"""
Question 2: Premium Burger
"""

"""
2.1 Most Expensive Burger
  Write the function to find
  the most expensive burger and the change
"""


def most_expensive_burger(money, price_dict):
    change, burger = money, ""
    price_list = sorted(price_dict.items(), key=lambda x: x[1], reverse=True)
    for i in range(len(price_list)):
        if price_list[i][1] > change:
            continue
        else:
            burger += price_list[i][0]
            change = change - price_list[i][1]
    if len(burger) == 0:
        return ("", change)
    else:
        return ("B" + burger + "B", change)


# Test data (do not modify)
price_list = {"C": 1, "V": 3, "P": 11, "A": 31}
# Test cases (comment out or remove before copying to Coursemology)
print(most_expensive_burger(0, {"C": 1, "V": 3, "P": 11, "A": 31}))
print(most_expensive_burger(25, {"C": 1, "V": 3, "P": 11, "A": 31}))
print(most_expensive_burger(
    55, {'C': 1, 'W': 2, 'I': 4, 'T': 9, 'O': 20, 'V': 41, 'S': 85}))
