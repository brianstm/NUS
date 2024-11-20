# Part 1


def encode_I(s1, s2, m):
    result = ''
    for i in range(len(s1)):
        result += chr((((ord(s1[i]) - ord('a')) +
                      int((s2[i])) * m) % 26) + ord('a'))
    return result


def encode_R(s1, s2, m):
    if s1 == "":
        return ""
    else:
        return chr((((ord(s1[0]) - ord('a')) + int((s2[0])) * m) %
                    26) + ord('a')) + encode_R(s1[1:], s2[1:], m)


def encode_U(s1, s2, m):
    return ''.join(chr((ord(s1[i]) - ord('a') + int(s2[i]) * m) 
                       % 26 + ord('a')) for i in range(len(s1)))


# print(encode_I('bye', '128', 2))
# print(encode_I('dcu', '128', -2))
# print(encode_I('spyxfamily', '2222222222', 1))
# print(encode_I('krmxhaeaba', '9170109981', -2))

# print(encode_R('bye', '128', 2))
# print(encode_R('dcu', '128', -2))
# print(encode_R('spyxfamily', '2222222222', 1))
# print(encode_R('krmxhaeaba', '9170109981', -2))

print(encode_U('bye', '128', 2))
print(encode_U('dcu', '128', -2))
print(encode_U('spyxfamily', '2222222222', 1))
print(encode_U('krmxhaeaba', '9170109981', -2))
