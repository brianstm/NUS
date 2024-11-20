# PE 01

"""
Question 3: Auspicious Numbers
"""

"""
3.1 Simple Auspicious
  Write the function to count how many
  numbers are auspicious numbers
"""


# def auspicious_number(n, bad):
#     min_value = 10 ** (n - 1)
#     max_value = (10 ** n) - 1
#     lst = [i for i in range(min_value, max_value+1)]
#     bad_num_lst = []
#     i = 1
#     for i in range(len(lst)):
#         for j in str(lst[i]):
#             for bad_num in bad:
#                 if str(j) == str(bad_num):
#                     bad_num_lst.append(lst[i])
#     new_lst = [i for i in lst if i not in bad_num_lst]
#     return len(new_lst)


def auspicious_number(n, bad):
    # amount of choices there are for first digit, from 1 to 9
    # 2, [1, 4] - 7 choices
    first_digit_choices = 9 - len(bad)
    # amount of choices there are for all digit, from 0 to 9
    # 2, [1, 4] - 8 choices
    remaining_digits_choices = 10 - len(bad)
    # total will be choices of first digit times the rest
    # pow is the number of possible choices for the remaining n-1 digits
    if 0 in bad:
        first_digit_choices += 1
    total = first_digit_choices * pow(remaining_digits_choices, n - 1)

    return total


def auspicious_number(n, bad):
    # Calculate the number of choices for the first digit.
    # The first digit cannot be a 'bad' number.
    # If the number of 'bad' digits is less than 9, add the difference to the total number of choices (9).
    # For example, if 'bad' is [1, 4], there are 7 choices for the first digit (1, 2, 3, 5, 6, 7, 8, 9).
    first_digit_choices = 9 - len(bad)

    # Calculate the number of choices for the remaining digits.
    # The remaining digits can be any number from 0 to 9, excluding the 'bad' numbers.
    # If the number of 'bad' digits is less than 10, subtract it from the total number of choices (10).
    # For example, if 'bad' is [1, 4], there are 8 choices for the remaining digits (0, 2, 3, 5, 6, 7, 8, 9).
    remaining_digits_choices = 10 - len(bad)

    # If 0 is a 'bad' number, add 1 to the number of choices for the first digit.
    # This is because 0 can be used as the first digit if it's not a 'bad' number.
    if 0 in bad:
        first_digit_choices += 1

    # Calculate the total number of possible auspicious numbers.
    # The total is the number of choices for the first digit times the number of choices for the remaining digits.
    # The number of choices for the remaining digits is raised to the power of (n - 1) because we're choosing n - 1 digits.
    total = first_digit_choices * pow(remaining_digits_choices, n - 1)

    return total


# Test cases (comment out or remove before copying to Coursemology)
print(auspicious_number(2, [4]))
print(auspicious_number(3, [4]))
print(auspicious_number(2, [1, 3]))
print(auspicious_number(3, [1, 3]))


"""
3.2 Efficient Auspicious
  Uncomment only if you are sure if your
  functions are efficient (finish within 1s)
  If your code runs for too long,
  press Ctrl + C on IDLE to stop it

  There is no need to submit separately
  for this part, marks will be awarded
  automatically if you can write an efficient
  solution to the Auspicious Numbers problem
"""
# Test cases (comment out or remove before submitting)
print(auspicious_number(50, [4]))
print(auspicious_number(1000, [1, 3]) % 1000000000)
print(auspicious_number(100000, [4]) % 1000000000)
