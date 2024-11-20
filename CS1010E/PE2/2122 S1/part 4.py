# PE2 Part 4


def child_DNA(n):
    dna = 1
    for i in str(n):
        dna *= int(i)
    return dna


# def parent_mutated_DNA(parent_original_dna):
#     child_dna = child_DNA(parent_original_dna)
#     i = 1
#     while True:
#         product = 1
#         for digit in str(i):
#             product *= int(digit)
#         if product == child_dna:
#             return i
#         i += 1

def parent_mutated_DNA(parent_original_dna):
    child_dna = child_DNA(parent_original_dna)
    i = 1
    while True:
        if child_DNA(i) == child_dna:
            return i
        i += 1


# def isMartian(d):
#     for possible_parent in range(1, d + 1):
#         if d % child_DNA(possible_parent) == 0:
#             return True
#     return False

def isMartian(d):
    for i in range(1, d + 1):
        if child_DNA(i) == d:
            return True
    return False


print(child_DNA(262))
print(child_DNA(987161))
print(child_DNA(982374972))

print(parent_mutated_DNA(262))
print(parent_mutated_DNA(12131))

print(isMartian(3024))
print(isMartian(16632))
