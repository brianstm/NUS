# PE 01

"""
Question 3: Valentine's Day Card
"""
from random import *
"""
3.1 Get Paint
  Write the function to calculate the area
"""


def paint_area(S, C, D):
    n = 10000
    m = 0

    pink_centers = [(0, S/2 - D/2), (S/2 - D/2, 0),
                    (0, -S/2 + D/2), (-S/2 + D/2, 0)]
    area_pink = (D / 2) ** 2
    area_white = (C / 2) ** 2

    for _ in range(n):
        x = uniform(-S/2, S/2)
        y = uniform(-S/2, S/2)

        is_in_pink = any((x - x_2)**2 + (y - y_2)**2 <=
                         area_pink for x_2, y_2 in pink_centers)

        is_in_white = x**2 + y**2 <= area_white

        if is_in_pink and not is_in_white:
            m += 1

    pink_area = (m/n) * (S**2)

    return pink_area


# Test cases (comment out or remove before copying to Coursemology)
print(paint_area(15, 8, 7))
print(paint_area(15, 8, 3))
