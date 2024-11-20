# PE 02

"""
Question 2: Catan
"""

"""
2.1 Player
"""


class Player():
    def __init__(self, color):
        self.color = color
        self.wood = 3
        self.brick = 3

    def get_colour(self):
        return self.color

    def get_resources(self):
        return (self.wood, self.brick)

    def robbed(self):
        if self.wood + self.brick < 8:
            return self.color + " is safe from robber"
        else:
            removed_wood = self.wood - (self.wood // 2)
            removed_brick = self.brick - (self.brick // 2)
            self.wood = self.wood // 2
            self.brick = self.brick // 2
            return self.color + " is robbed of " + str(removed_wood + removed_brick) + " resources"

    def trade(self, other_player, woods, bricks):
        if self.wood < woods:
            return self.color + " does not have enough wood"
        elif other_player.brick < bricks:
            return other_player.color + " does not have enough brick"
        else:
            self.wood -= woods
            self.brick += bricks
            other_player.wood += woods
            other_player.brick -= bricks
            return self.color + " trades with " + other_player.color

    def build(self, tile):
        if self.wood < 2 or self.brick < 2:
            return self.color + " does not have enough resources to build"
        elif tile.building > 3:
            return "Tile " + str(tile.number) + " does not have any space"
        else:
            self.wood -= 2
            self.brick -= 2
            tile.add_building(self)
            return self.color + " builds on Tile " + str(tile.number)


"""
2.2 Tile
"""


class Tile():
    def __init__(self, number, resource):
        self.number = number
        self.resource = resource
        self.building = 0
        self.builders = []

    def get_number(self):
        return int(self.number)

    def get_resources(self):
        return self.resource

    def get_building(self):
        return int(self.building)

    def produce(self):
        if self.building == 0:
            return "Tile " + str(self.number) + " does not produce any " + self.resource
        else:
            for player in self.builders:
                if self.resource == "wood":
                    player.wood += 1
                else:
                    player.brick += 1
            return "Tile " + str(self.number) + " produces " + \
                str(self.building) + " " + self.resource

    def add_building(self, player):
        self.building += 1
        self.builders.append(player)


# Test data (do not modify)
red = Player("Red")
blue = Player("Blue")
yellow = Player("Yellow")
brick1 = Tile(1, "brick")
wood1 = Tile(2, "wood")
brick2 = Tile(3, "brick")
wood2 = Tile(4, "wood")
# Test cases (comment out or remove before copying to Coursemology)
print(red.build(brick1))
print(brick1.produce())
print(red.build(wood1))
print(blue.build(wood1))
print(yellow.build(brick1))
print(brick1.produce())
print(brick1.produce())
print(wood2.produce())
print(wood1.produce())
print(wood1.produce())
print(wood1.produce())
print(blue.get_resources())
print(red.get_resources())
print(blue.trade(red, 5, 1))
print(blue.trade(red, 1, 5))
print(blue.trade(red, 2, 2))
print(blue.get_resources())
print(red.get_resources())
