def RLD_I(s):
    result = ''
    for i in range(0, len(s), 2):
        result += s[i] * int(s[i+1])

    return result


def RLD_R(s):
    result = ''
    if s == '':
        return ''
    else:
        result += s[0] * int(s[1])
        return result + RLD_R(s[2:])


print(RLD_I('H3e2l3o1W1o3r4l2d1'))
print(RLD_I('A9H3E2M1'))
print(RLD_R('H3e2l3o1W1o3r4l2d1'))
print(RLD_R('A9H3E2M1'))
