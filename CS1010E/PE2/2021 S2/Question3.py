# PE 02

"""
Question 3: Maze
"""


def create_zero_matrix(r, c):
    return [[0]*c for _ in range(r)]


def get_row(m):
    return len(m)


def get_col(m):
    return len(m[0])


def m_tight_print(m):
    for row in m:
        print(f'{"".join(map(str,row))}')


"""
3.1 Amazing Slide
  Write the function to check if
  you can slide
"""


def is_solvable(maze):
    # DFS, but each neighbour is the first reachable stone in 4 directions
    rows, cols = get_row(maze), get_col(maze)

    def get_neighbours(i, j):
        # Given coordinate (i, j), returns a list of at most 4 coordinates
        # Each coordinate is a reachable neighbour (stone) from current coordinate
        neighbours = []
        # Up
        for ii in range(i+1, rows):
            if maze[ii][j]:
                neighbours.append((ii, j))
                break
        # Down
        for ii in range(i-1, 0, -1):
            if maze[ii][j]:
                neighbours.append((ii, j))
        # Right
        for jj in range(j+1, cols):
            if maze[i][jj]:
                neighbours.append((i, jj))
                break
        # Left
        for jj in range(j-1, 0, -1):
            if maze[i][jj]:
                neighbours.append((i, jj))
                break
        return neighbours
    # DFS
    stack = [(0, 0)]
    goal = (rows-1, cols-1)
    visited = set([(0, 0)])
    while stack:
        i, j = stack.pop()
        for neighbour in get_neighbours(i, j):
            if neighbour == goal:
                return True
            if neighbour in visited:
                continue
            stack.append(neighbour)
            visited.add(neighbour)

    return False


# Test data (do not modify)
maze1 = [[1, 0, 0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0, 0, 1],
         [0, 1, 0, 0, 1, 0, 0],
         [0, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1]]

maze2 = [[1, 0, 0, 0, 1, 0, 0],
         [0, 0, 0, 0, 0, 0, 1],
         [0, 1, 0, 0, 1, 0, 0],
         [0, 1, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1]]

# Test cases (comment out or remove before copying to Coursemology)
print(is_solvable(maze1))
print(is_solvable(maze2))
