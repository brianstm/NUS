# PE 01

"""
Question 1: Encoding
"""

"""
1.1 Iterative Encoding
  Write the function to encode iteratively
"""


# def encode_I(word):
#     encoded_word = ''
#     for i in word:
#         if i == ' ':
#             encoded_word += '99'
#         else:
#             encoded_num = ord(i) - 65
#             encoded_word += str(encoded_num).zfill(2)
#     return encoded_word

def encode_I(word):
    letter_to_number = {'A': '00', 'B': '01', 'C': '02', 'D': '03', 'E': '04', 'F': '05', 'G': '06', 'H': '07', 'I': '08', 'J': '09', 'K': '10', 'L': '11', 'M': '12',
                        'N': '13', 'O': '14', 'P': '15', 'Q': '16', 'R': '17', 'S': '18', 'T': '19', 'U': '20', 'V': '21', 'W': '22', 'X': '23', 'Y': '24', 'Z': '25', ' ': '99'}
    encoded_word = ''

    for char in word:
        encoded_word += letter_to_number[char]
    return encoded_word


# Test cases (comment out or remove before copying to Coursemology)
print(encode_I('HI SALLY'))
print(encode_I('I MISS YOU'))
print(encode_I('ARE YOU FREE FOR DINNER TONIGHT'))


"""
1.2 Recursive Encoding
  Write the function to encode recursively
"""


# def encode_R(word):
#     encoded_word = ''
#     if word == '':
#         return ''
#     else:
#         i = word[0]
#         if i == ' ':
#             encoded_word += '99'
#         else:
#             encoded_num = ord(i) - 65
#             encoded_word += str(encoded_num).zfill(2)
#         return encoded_word + encode_R(word[1:])

def encode_R(word):
    encoded_word = ''
    letter_to_number = {'A': '00', 'B': '01', 'C': '02', 'D': '03', 'E': '04', 'F': '05', 'G': '06', 'H': '07', 'I': '08', 'J': '09', 'K': '10', 'L': '11', 'M': '12',
                        'N': '13', 'O': '14', 'P': '15', 'Q': '16', 'R': '17', 'S': '18', 'T': '19', 'U': '20', 'V': '21', 'W': '22', 'X': '23', 'Y': '24', 'Z': '25', ' ': '99'}
    if word == '':
        return ''
    else:
        encoded_word += letter_to_number[word[0]]
        return encoded_word + encode_R(word[1:])


# Test cases (comment out or remove before copying to Coursemology)
print(encode_R('HI SALLY'))
print(encode_R('I MISS YOU'))
print(encode_R('ARE YOU FREE FOR DINNER TONIGHT'))
