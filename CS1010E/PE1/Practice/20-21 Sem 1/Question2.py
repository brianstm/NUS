# PE 01

"""
Question 2: Decoding Messages
"""

"""
2.1 Offset Decoding
  Write the function to decode the message
  knowing the offset
"""


def decode(msg, offset):
    result = ''
    number_to_letter = {'00': 'A', '01': 'B', '02': 'C', '03': 'D', '04': 'E', '05': 'F', '06': 'G', '07': 'H', '08': 'I', '09': 'J', '10': 'K', '11': 'L',
                        '12': 'M', '13': 'N', '14': 'O', '15': 'P', '16': 'Q', '17': 'R', '18': 'S', '19': 'T', '20': 'U', '21': 'V', '22': 'W', '23': 'X', '24': 'Y', '25': 'Z'}
    for i in range(0, len(msg), 2):
        if msg[i:i+2] == '99':
            result += ' '
        else:
            number = str(int(msg[i:i+2]) - offset).zfill(2)
            while int(number) < 0:
                number = str(int(number) + 26).zfill(2)
            result += number_to_letter[number]

    return result


# Test cases (comment out or remove before copying to Coursemology)
print(decode('1213992305161603', 5))
print(decode('0007159919102399170713991207221917', 123))
print(decode('190008991213000605992416160599002599110000249905002520181905', 12))
print(decode('2107062510191213041912010706991707139911070414232299120001119908191012', 71))


"""
2.2 Secret Decoding
  Write the function to decode the message
  without knowing the offset
"""


def decode_with_love(msg):
    i = 0
    while True:
        decoded_msg = decode(msg, i)
        i += 1
        if "LOVE" in decoded_msg:
            return decoded_msg


# Test cases (comment out or remove before copying to Coursemology)
print(decode_with_love('0906190699021906992109069920161508209924069913162306'))
print(decode_with_love('011607111713129925120299011013200316'))
print(decode_with_love('0819199906220299211212119916009919220312'))
print(decode_with_love('0710170099080099150009250013'))
print(decode_with_love(
    '16040515991201990515991011160405100399240102111401991117149908111801'))
