# Part 1
engineering = 'MMFMFFMMMF'
history = 'FFMMFFFFMFF'
business = 'FFFMMMFFMMFMFMFM'

def how_many_male(faculty):
    count = 0
    for i in faculty:
        if i == 'M':
            count += 1
    return count


def how_many_female(faculty):
    count = 0
    for i in faculty:
        if i == 'F':
            count += 1
    return count


def gender_balance(faculty):
    if how_many_male(faculty) > how_many_female(faculty):
        return 'male'
    elif how_many_male(faculty) < how_many_female(faculty):
        return 'female'
    elif how_many_male(faculty) == how_many_female(faculty):
        return 'balanced'


print(how_many_male(history))
print(how_many_female(engineering))
print(gender_balance(engineering))
print(gender_balance(history))
print(gender_balance(business))


