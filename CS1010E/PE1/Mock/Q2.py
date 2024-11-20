# Part 2
def caterpillar(n):
    result = ''
    for _ in range(n-1):
        result += 'Q'

    result += '6'
    return result


def caterpillar_with_backside(n):
    result = 'c'
    for _ in range(n-2):
        result += 'Q'
        
    result += '6'
    return result


print(caterpillar(4))
print(caterpillar(10))
print(caterpillar_with_backside(10))
