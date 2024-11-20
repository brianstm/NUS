def num_divisor_list(N):
    result = [0] * (N + 1)
    for i in range(1, N + 1):
        j = i
        while j <= N:
            result[j] += 1
            j += i
    return result


def list_of_max_divisor(N):
    divisors = num_divisor_list(N)
    max_divisors = max(divisors)
    return sorted([i for i, d in enumerate(divisors) if d == max_divisors])


def how_many_prime(N):
    count = 0
    for i in range(2, N+1):
        if all(i % j != 0 for j in range(2, int(i**0.5) + 1)):
            count += 1
    return count


print(num_divisor_list(6))
print(num_divisor_list(10))
print(num_divisor_list(50))

print(list_of_max_divisor(10))
print(list_of_max_divisor(25))
print(list_of_max_divisor(98))

print(how_many_prime(25))
print(how_many_prime(100))
print(how_many_prime(1000))
