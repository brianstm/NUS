# PE 02

"""
Question 3: Game of Life
"""


def create_zero_matrix(n, m):
    return [[0 for i in range(m)] for j in range(n)]


def m_tight_print(m):
    for row in m:
        print(''.join(map(str, row)))


def m_tight_print_gof(m):
    for row in m:
        print(''.join(map(lambda x: '#' if x == 1 else '_', row)))


"""
3.1 Add cells
  Write the function to add cells
"""


def add_cells(board, cell_list):
    for i in cell_list:
        if 0 <= i[0] < len(board) and 0 <= i[1] < len(board[0]):
            board[i[0]][i[1]] = 1


# Test data (do not modify)
very_long_house = [(5, 6), (5, 7), (5, 8), (5, 9), (5, 10),
                   (6, 5), (6, 8), (6, 11), (7, 5), (7, 6), (7, 10), (7, 11)]
board = create_zero_matrix(2, 3)
board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
add_cells(board, [(1, 3), (-1, 1), (3, 2)])
m_tight_print(board)

# m_tight_print(board)
# Test cases (comment out or remove before copying to Coursemology)
# add_cells(board, [(1, 2), (1, 1), (1, 0)])
# m_tight_print(board)
# add_cells(board, [(0, 1), (1, 1)])
# m_tight_print(board)


"""
3.2 Simulate
  Write the function to
  simulate game of life
"""


# def step(board):
#     rows = len(board)
#     cols = len(board[0])
#     new_board = [[0]*cols for _ in range(rows)]

#     for i in range(rows):
#         for j in range(cols):
#             neighbor = 0
#             for x in range(max(0, i - 1), min(rows, i + 2)):
#                 for y in range(max(0, j - 1), min(cols, j + 2)):
#                     neighbor += board[x][y]

#             neighbor -= board[i][j]

#             if board[i][j] == 1 and (neighbor == 2 or neighbor == 3):
#                 new_board[i][j] = 1
#             elif board[i][j] == 0 and neighbor == 3:
#                 new_board[i][j] = 1
#     return new_board


# TRY 1
# def step(board):
#     rows = len(board)
#     cols = len(board[0])
#     new_board = create_zero_matrix(rows, cols)
#     neighbor = 0
#     for i in range(rows):
#         for j in range(cols):
#             neighbor = 0
#             if j < cols - 1:
#                 neighbor += board[i][j + 1]
#             if j > 0:
#                 neighbor += board[i][j - 1]
#             if i < rows - 1:
#                 neighbor += board[i + 1][j]
#             if i > 0:
#                 neighbor += board[i - 1][j]
#             if i < rows - 1 and j < cols - 1:
#                 neighbor += board[i + 1][j + 1]
#             if i < rows - 1 and j > 0:
#                 neighbor += board[i + 1][j - 1]
#             if i > 0 and j < cols - 1:
#                 neighbor += board[i - 1][j + 1]
#             if i > 0 and j > 0:
#                 neighbor += board[i - 1][j - 1]

#             if board[i][j] == 1:
#                 if neighbor <= 1:
#                     new_board[i][j] = 0
#                 elif neighbor >= 4:
#                     new_board[i][j] = 0
#                 elif neighbor == 2 or neighbor == 3:
#                     new_board[i][j] = 1

#             elif board[i][j] == 0:
#                 if neighbor == 3:
#                     new_board[i][j] = 1
#                 else:
#                     continue
#     return new_board


# TRY 2
def step(board):
    rows = len(board)
    cols = len(board[0])
    new_board = create_zero_matrix(rows, cols)
    neighbor = 0
    for i in range(rows):
        for j in range(cols):
            neighbor = 0
            for x in range(max(0, i - 1), min(rows, i + 2)):
                for y in range(max(0, j - 1), min(cols, j + 2)):
                    neighbor += board[x][y]

            neighbor -= board[i][j]

            if board[i][j] == 1 and neighbor <= 1 and neighbor >= 4:
                new_board[i][j] = 0
            if board[i][j] == 1 and (neighbor == 2 or neighbor == 3):
                new_board[i][j] = 1

            elif board[i][j] == 0 and neighbor == 3:
                new_board[i][j] = 1
    return new_board


# Test data (do not modify)
board0 = [[1, 1, 0, 0],
          [1, 1, 1, 1],
          [0, 1, 0, 0]]
# Test cases (comment out or remove before copying to Coursemology)
# m_tight_print(board0)
# print("")
# board1 = step(board0)
# m_tight_print(board1)
# print("")
# board2 = step(board1)
# m_tight_print(board2)
