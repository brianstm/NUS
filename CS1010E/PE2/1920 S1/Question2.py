# PE 02

"""
Question 2: Pizza Delivery 2.0
"""


def m_tight_print(m):
    for row in m:
        print(''.join(row))


"""
2.1 PizzaShop
  Implement the class PizzaShop
"""


class PizzaShop:
    def __init__(self, pos, name, radius, hour_s, hour_e):
        self.pos = pos
        self.name = name
        self.radius = radius
        self.hour_s = hour_s
        self.hour_e = hour_e

    def distance_square_to(self, i, j):
        return (self.pos[0] - i) ** 2 + (self.pos[1] - j) ** 2


"""
2.2 Delivery Map 2.0
  Update delivery map
  to use class
"""


def create_zero_matrix(n, m):
    return [[0 for i in range(m)] for j in range(n)]


def pd_map(r, c, all_shops, hour):
    map = create_zero_matrix(r, c)
    # Iterate over each cell in the map
    for i in range(r):
        for j in range(c):
            # Initialize the minimum distance to the maximum possible distance
            min_dist = r**2 + c**2
            # Initialize the nearest shop to None
            min_shop = None
            # Iterate over each PizzaShop in all_shops
            for shop in all_shops:
                # Calculate the square of the distance from the shop to the cell
                dist = shop.distance_square_to(i, j)
                # Check if the shop can deliver to the cell at the given hour
                if (dist <= shop.radius**2 and shop.hour_s <= hour < shop.hour_e):
                    # If the distance from the shop to the cell is less than the 
                    # current minimum distance
                    if dist < min_dist:
                        # Update the minimum distance and the nearest shop
                        min_dist = dist
                        min_shop = shop
                    # If the distance from the shop to the cell is equal to the 
                    # current minimum distance
                    elif dist == min_dist:
                        # Mark the cell as equidistant from multiple shops
                        min_shop = 'X'
            # If the cell is equidistant from multiple shops or not reachable by any shop
            if min_shop == 'X' or min_shop is None:
                # Mark the cell accordingly
                map[i][j] = min_shop if min_shop == 'X' else '.'
            else:
                # If the cell is reachable by a single shop, mark the cell with the 
                # first character of the shop's name
                map[i][j] = min_shop.name[0]
    # Return the completed map
    return map


# Test data (do not modify)
all_shop = [PizzaShop([3, 3], 'Ace', 3, 8, 14),
            PizzaShop([6, 6], 'Bizza', 4, 12, 22)]
# Test cases (comment out or remove before copying to Coursemology)
m_tight_print(pd_map(10, 12, all_shop, 10))
m_tight_print(pd_map(10, 12, all_shop, 12))
m_tight_print(pd_map(10, 12, all_shop, 16))
