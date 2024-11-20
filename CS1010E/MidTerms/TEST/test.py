# x = 20
# n = int(input())
# if n != 0 and x // n > 6:
#     x += 1
# else:
#     x %= n
# print(x)

# x = 5
# n = int(input())
# if n < 0 or not (n % 2) or x // n < 6:
#     x += 1
# else:
#     x //= 2
# print(x)

# def count4(n):
#     cnt = [0] * 4
#     for i in range(n+1):
#         if i % 2 == 0:
#             if i % 6 == 0:
#                 cnt[0] += 1
#                 print("A", i)
#             else:
#                 cnt[1] += 1
#                 print("B", i)
#         elif i % 3 == 0:
#             cnt[2] += 1
#             print("C", i)
#         else:
#             cnt[3] += 1
#             print("D", i)
#     return cnt


# print(count4(50))

# x = 1
# y = 1
# while (x < 300):
#     print(x, y)
#     x *= 3
#     y += 1

# print(x)


# def ordered(lst):
#     j = len(lst)-1
#     i = 0
#     while (i < j):
#         if lst[i] == 0:
#             i += 1
#         elif lst[j] == 1:
#             j -= 1
#         else:
#             lst[i], lst[j] = lst[j], lst[i]


# list1 = [0, 1, 0, 1, 0, 0, 1, 0]
# ordered(list1)
# print(list1)

from turtle import *
dd = {1: {2: 3}, 2: {3: 1}, 3: {1: 3}}
print(dd[2][3])  # 1
print(dd[dd[2][3]])  # {2: 3}
# The max function is applied to the keys of the dictionary {2: 3}, and the maximum key is 2, so it prints 2.
print(max(dd[dd[2][3]]))

s1 = '1234567890'
print(s1[8:2:-12])  # 9
print(s1[-2:2:-2])  # 975
print(s1[8:-7:-2])  # 975
print(s1[8:3:-2])  # 975
print(s1[-2:3:-2])  # 975
print(s1[8:4:-2])  # 97


def rec(stg, acc):
    if stg:
        return rec(stg[1:], acc+'a')+'b'
    else:
        return acc

# First call: stg='1234', acc=''
# Calls rec('234', 'a') + 'b'
#   Second call: stg='234', acc='a'
#   Calls rec('34', 'aa') + 'b'
#       Third call: stg='34', acc='aa'
#       Calls rec('4', 'aaa') + 'b'
#           Fourth call: stg='4', acc='aaa'
#           Calls rec('', 'aaaa') + 'b'
#               Fifth call: stg='', acc='aaaa'
#               Returns 'aaaa'
#           Returns 'aaaab'
#       Returns 'aaaabb'
#   Returns 'aaaabbb'
# Returns 'aaaabbbb'


print(rec('1234', ''))


def circle(f, g):
    return lambda x: g(f(x))


def g(x): return (x, x)


h = circle(g, g)
print(h(3)) # ((3, 3), (3, 3))


dict = {1: 'Z', 2: 'MAX', 3: 'IS', 4: 'DEF', 5: 'UN', 6: 'A'}
print(dict[max(dict)] == min(dict.values()), dict[3] == dict.pop(
    3), dict.pop(min(dict.keys())) == max(dict.values()))
# max(dict) returns the maximum key in the dictionary, which is 6.
# min(dict.values()) returns the minimum value in the dictionary values, which is 'A'.
# dict[max(dict)] == min(dict.values()):
#   This is equivalent to dict[6] == 'A', which is True.
# dict[3] == dict.pop(3):
#   This is equivalent to 'IS' == dict.pop(3), which removes the key 3 and returns its value 'IS'. So, this expression evaluates to True.
# dict.pop(min(dict.keys())) == max(dict.values()):
#   min(dict.keys()) returns the minimum key, which is 1.
#   dict.pop(1) removes the key 1 and returns its value 'Z'.
#   So, this expression is equivalent to 'Z' == max(dict.values()), which is False.


dd = {'a': 0, 'b': 1, 'c': 2, 'd': 0, 'e': 1, 'f': 2}


def valKeys(dict, valLst):
    kys = []
    for val in valLst:
        kys.extend([k for (k, val) in dict.items()])
    return kys


print(valKeys(dd, [0, 2])) # ['a', 'b', 'c', 'd', 'e', 'f', 'a', 'b', 'c', 'd', 'e', 'f']

# print(list((1)) + list([2]) + list('3'))
# TypeError: 'int' object is not iterable list((1))

t1 = [1, 2, 3]
t2 = (t1, t1)
t2[0][2] = 0
print(t2)  # ([1, 2, 0], [1, 2, 0])


def foo(x):
    return lambda x: x+x


print(foo(5)(2))  # 4


def chking(seq):
    d = list(seq)
    b = len(seq)
    for a in range(b-1):
        for i in d:
            if i == d[a:b]:
                # will never get executed because i is an element of d, and it's not possible for an element to be equal to a sublist d[a:b].
                return False
            elif i >= max(d[a+1:b]):
                return True
            else:
                return False
    return True


[5, [3], [2, 3]][[2, 1][0]][:[1, 2][1]]  # [2, 3]
# Steps:
# [[2, 1][0]]  # [2]
# [:[1, 2][1]]  # [:2]
# [5, [3], [2, 3]][2][:2]
# [2, 3][:2]  # [2, 3]


(lambda a, b: lambda x: b(x(a)))('a', lambda a: a*2)(lambda a: a[1:])  # ''
# Steps:
# (lambda a, b: lambda x: b(x(a)))('a', lambda a: a*2)
# lambda x: (lambda a: a*2)(x('a'))
# (lambda a: a*2)('a'[1:])
# (lambda a: a*2)('')


x = [1, 2, 3]


def foo(l, x):
    if not l:
        return l
    return foo(l[1:], x) + [x(l[0])]


print(foo(x, lambda x: 4-x))  # [1, 2, 3] it appends to the back of the list


x = {'a', 'bc', 'de'}
y = {'b', 'de', 'a', 'b'}
# {'bc', 'b'} symmetric difference means the elements that are in one set but not the other
print(x ^ y)

# & 	AND	    Sets each bit to 1 if both bits are 1
# |	    OR	    Sets each bit to 1 if one of two bits is 1
# ^	    XOR	    Sets each bit to 1 if only one of two bits is 1
# ~	    NOT	    Inverts all the bits
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off	x << 2
# >>	Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off	x >> 2


def evenDigits(N):
    if N == 0:
        return 0
    if N % 2 == 0:
        return evenDigits(N//10)*10+N % 10
    else:
        return evenDigits(N//10)


print(evenDigits(123456))  # 246
print(evenDigits(12332401))  # 2240

# In a dictionary in Python, The values can be any data type

print(6-------6)  # 0

print(6-True+False**0)  # 6 - 1 + 0^0 = 6 - 1 + 1 = 6

print(8/4*2)  # 4.0

print('1234567'[2:5][1:2][1:])  # ""
'1234567'[2:5]  # 345
'1234567'[2:5][1:2]  # 4
'1234567'[2:5][1:2][1:]  # ""

# tuple('xyz')+tuple((3))  # 3 is not iterable

print([1, 2, [3, 4], 5, 6][[1, 2, 4][2]:[1, 2, 3, 4, 5][3]])  # []
[1, 2, [3, 4], 5, 6][4:4]

# lambda no return statement
# (lambda x,y,z:return x-y+z)(3,2,1) # SyntaxError: 'return' outside function

# 17//2 + 17//2//2 = 8 + 4 = 12
print((lambda x, y: y(y(x))+y(x))(17, lambda x: x//2))

print((lambda x: x((lambda x: x(lambda x: x))(x(x))))
      (lambda x: x)(lambda x: x+x)(3))  # 3+3 = 6 the rest is just x = x


# def f1(x):
#     return 1+f3(x)
# def f3(x):
#     return 1+f1(x)
# f1(4) # RecursionError: maximum recursion depth exceeded in comparison

# def f1(x):
#     return '1'+f2(x)
# def f2(x):
#     return f3(x)+'2'
# def f3(x):
#     return '3'+f4(x)
# def f4(x):
#     return '4'+x
# f1(0) # Error because '4' (str) + 0 (int) is not possible

x = ['a', 'b', 'c', 'd']


def foo(l, f):
    if not l:
        return l
    return foo(f(l[1:]), f)+[f(l[0])]


print(foo(x, lambda x: x[::-1]))  # ['c', 'b', 'd', 'a']

lst1 = ['bc', 'de', 'ya', 'ab', 'bq', 'bd']
lst2 = []
for x in lst1:
    lst2.append(tuple(x))
# d = dict(lst2) # dict object is not callable
# [('b', 'c'), ('d', 'e'), ('y', 'a'), ('a', 'b'), ('b', 'q'), ('b', 'd')]
print(lst2)


x = {'a', 'bc', 'de', 'a'}
y = {'b', 'de', 'a', 'a', 'b'}
print(x ^ y)  # {'b', 'bc'} one have other dont
print(y-x ^ y)  # {'de', 'a'} remove from y
print(x | y-x ^ y)  # {'de', 'a', 'bc'} OR against x


def foo(L):
    for i in range(len(L)-1):
        for j in range(len(L)-i):
            if L[j] > L[j+1]:  # +1 will eventually go out of range
                L[j], L[j+1] = L[j+1], L[j]

# three data types cannot be used as keys in a Python dictionary: list, dict, and set.
