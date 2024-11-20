from math import factorial


def localPeak(lst):
    l = len(lst)
    if lst[0] > lst[1]:
        return 0
    for i in range(1, l-1):
        if lst[i] > lst[i+1] and lst[i] > lst[i-1]:
            return i
    if lst[l-1] > lst[l-2]:
        return l-1


# print(localPeak([1, 5, 6, 9, 5, 4, 3, 10, 11]))  # 3
# print(localPeak([1, 2, 3, 4, 5]))  # 4
# print(localPeak([10, 9, 8, 7]))  # 0


def sinhU(x):
    def sf(n):
        return x ** (2 * n + 1) / factorial(2 * n + 1)
    return sum(map(sf, range(0, 50)))


print(sinhU(5))
