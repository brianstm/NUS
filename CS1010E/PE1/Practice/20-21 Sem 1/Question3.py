# PE 01

"""
Question 3: Famous Painting
"""

"""
3.1 Simple Area
  Write the function to calculate the area
"""


# def calculate_areas(w_list, h_list):
#     color_index = 0
#     white = 0
#     yellow = 0
#     red = 0
#     for i in w_list:
#         for j in h_list:
#             if color_index == 0:
#                 white += i * j
#             elif color_index == 1:
#                 yellow += i * j
#             elif color_index == 2:
#                 red += i * j
#             if color_index > 1:
#                 color_index = 0
#             else:
#                 color_index += 1

#     return (white, yellow, red)


# def calculate_areas(w_list, h_list):
#     areas = [0, 0, 0]

#     for i in range(len(w_list)):
#         for j in range(len(h_list)):
#             area = w_list[i] * h_list[j]

#             color = (i + j) % 3
#             areas[color] += area

#     return tuple(areas)


def calculate_areas(w_list, h_list):
    # Initialize the variables for each color
    white, yellow, red = 0, 0, 0
    # Create a dictionary to store the heights for each color
    color_dict = {i: 0 for i in range(3)}

    # Loop through the height list and add the heights to the corresponding color in the dictionary
    for i in range(len(h_list)):
        color_dict[i % 3] += h_list[i]

    for i in range(len(w_list)):
        # Calculate the offset to ensure the colors are distributed evenly
        offset = i % 3
        # Calculate the area for each color
        white += w_list[i] * color_dict[(i + offset) % 3]
        yellow += w_list[i] * color_dict[(i + 1 + offset) % 3]
        red += w_list[i] * color_dict[(i + 2 + offset) % 3]

    # Return the calculated areas
    return (white, yellow, red)


# Test data
l1 = [6, 2, 4, 5, 1, 1, 4]
l2 = [2, 5, 1, 4, 2, 3, 4]
l3 = [1]*10
# Test cases (comment out or remove before copying to Coursemology)
print(calculate_areas((1, 1, 1), (1, 1, 1)))
print(calculate_areas(l1, l2))
print(calculate_areas(l3, l3))


"""
3.2 Efficient Area
  Uncomment only if you are sure if your
  functions are efficient (finish within 1s)
  If your code runs for too long,
  press Ctrl + C on IDLE to stop it

  There is no need to submit separately
  for this part, marks will be awarded
  automatically if you can write an efficient
  solution to the Area problem
"""
# Test data
l4 = [i for i in range(100000)]
# Test cases (comment out or remove before submitting)
# print(calculate_areas(l4, l4[::-1]))
# print(calculate_areas(l4, l4))
