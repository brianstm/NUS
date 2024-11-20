# PE2 Part 2


def per_cipher_i(s, n):
    result = ''
    for i in range(0, len(s), n):
        result += s[i:i+n][::-1]
    return result


def per_cipher_r(s, n):
    if s == '':
        return s
    else:
        return s[:n][::-1] + per_cipher_r(s[n:], n)


def per_cipher_o(s, n):
    return ''.join(s[i:i+n][::-1] for i in range(0, len(s), n))


print(per_cipher_i('PYTHON CODING IS VERY USEFUL', 4))
print(per_cipher_i('12345678910', 3))
print(per_cipher_i(per_cipher_i('12345678910', 3), 3))
print(per_cipher_i('PE Part 1 is supposed to be easy', 7))

print(per_cipher_r('PYTHON CODING IS VERY USEFUL', 4))
print(per_cipher_r('12345678910', 3))
print(per_cipher_r(per_cipher_r('12345678910', 3), 3))
print(per_cipher_r('PE Part 1 is supposed to be easy', 7))

print(per_cipher_o('PYTHON CODING IS VERY USEFUL', 4))
print(per_cipher_o('12345678910', 3))
print(per_cipher_o(per_cipher_o('12345678910', 3), 3))
print(per_cipher_o('PE Part 1 is supposed to be easy', 7))
