# Part 2

def preparemaps():  # run this to generate two text file, map1.txt and map2.txt
    m1 = ['WWWWWWWWWWWWWWWWWW.WWWWWWW',
          'WWWWWWWW.WWWWWWWW...WWWWWW',
          'WWWWW...WWWWWWWWWW.B..WWWW',
          'WWWWWWW.WWWWWWWWW...WWWWWW',
          'WWWWWWW.....WWWWWWWW..WWWW',
          'WWW.......WWWWWWWWWWWWWWWW',
          'WWWW...A..WWWWWWWWWWW..WWW',
          'WWWWW.....WWWWWWWW...WWWWW',
          'WWWWWWW..WWWWWWWWW.C.WWWWW',
          'WWWW..WWWWWWWWWWWW...WWWWW',
          'WW....WWWWWWWWWWWWWWWWWWWW',
          'WWW.WWWWWWWWWWWWWWWWWWWWWW']
    map1file = open('map1.txt', 'w')
    for r in m1:
        map1file.write(r+'\n')
    m2 = ['WWWWWWWWWWWWWWW.WWWWWWW',
          'WWWWW.WWWWWWWW...WWWWWW',
          'WWWWWWWWWWWWWWW.B..WWWW',
          'WWWW.WW.WWWWWW...WWWWWW',
          'WWWW...WWWWWWWWWW..WWWW',
          'W......WWWWWWWWWWWWWWWW',
          'W...A..WWWWWWWWWWW..WWW',
          'WW.....WWWWWWWW...WWWWW',
          'WWWWWWWWWWWWWWWWWWWWWWW']
    map2file = open('map2.txt', 'w')
    for r in m2:
        map2file.write(r+'\n')


# This will read in a file and covert it into a 2D array
# You do not need to use it if you have another way to solve Part 2
# However, if you use this code, please remember to include in your submission
def readmap(filename):
    f = open(filename)
    m = []
    for line in f:
        m.append(list(line.rstrip('\n')))
    return m


preparemaps()


def crop_map(filename, minr, maxr, minc, maxc):
    mapped = readmap(filename)
    cropped = []
    for i in range(maxr-minr):
        cropped.append(''.join(mapped[minr+i][minc:maxc]))
    return cropped


def island_area(filename, prince):
    map_data = readmap(filename)
    # Find the prince's position
    for r, row in enumerate(map_data):
        for c, cell in enumerate(row):
            if cell == prince:
                start = (r, c)
                break
    # If the prince's character was not found in the map, return 0
    if not start:
        return 0
    # Use BFS to find all the connected land cells
    area = 0
    queue = [start]
    visited = set()
    while queue:
        r, c = queue.pop(0)
        if (r, c) not in visited and 0 <= r < len(map_data) and \
                0 <= c < len(map_data[0]) and map_data[r][c] != 'W':
            area += 1
            visited.add((r, c))
            queue.extend([(r-1, c), (r+1, c), (r, c-1), (r, c+1)])
    return area


def prince_map(filename, prince):
    map_data = readmap(filename)
    # Find the prince's position
    for r, row in enumerate(map_data):
        for c, cell in enumerate(row):
            if cell == prince:
                start = (r, c)
                break
    # If the prince's character was not found in the map, return []
    if not start:
        return []
    # Use BFS to find all the connected land cells and their bounds
    minr = minc = float('inf')
    maxr = maxc = float('-inf')
    queue = [start]
    visited = set()
    while queue:
        r, c = queue.pop(0)
        if (r, c) not in visited and 0 <= r < len(map_data) and \
                0 <= c < len(map_data[0]) and map_data[r][c] != 'W':
            minr = min(minr, r)
            maxr = max(maxr, r)
            minc = min(minc, c)
            maxc = max(maxc, c)
            visited.add((r, c))
            queue.extend([(r-1, c), (r+1, c), (r, c-1), (r, c+1)])
    # Crop the map according to the found indices and return the result
    cropped_map = [row[minc:maxc+1] for row in map_data[minr:maxr+1]]
    cropped_map_str = [''.join(row) for row in cropped_map]
    return cropped_map_str

# print(crop_map("map1.txt", 5, 9, 3, 25))
# print(crop_map("map1.txt", 7, 10, -10, 40))
# print(crop_map("map1.txt", 3, 3, 4, 4))
# print(crop_map("map1.txt", -10, 100, 3, 4))


print(island_area("map1.txt", "A"))
print(island_area("map1.txt", "B"))
print(island_area("map1.txt", "C"))
print(island_area("map2.txt", "A"))

print(prince_map('map1.txt', 'A'))
print(prince_map('map1.txt', 'B'))
print(prince_map('map1.txt', 'C'))
